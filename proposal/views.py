from datetime import timedelta, datetime, timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Proposal, WorkDaysSchedule, Post, Days
from .forms import ProposalForm
from django.contrib.auth.decorators import user_passes_test

week_days_name = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье'
]


def count_intervals(start_time, end_time):
    # Функция возвращает количество временных слотов
    return int((end_time - start_time).seconds / 60 / 20)

def generate_time(start_time, iteration):
    # Генерация времени с учетом интервала в 20 минут
    return start_time + timedelta(minutes=20 * iteration)


def get_available_time_slots(doctor, user, selected_day=None):
    if not selected_day:
        return []

    # Получение доступных временных слотов для записи к врачу
    # selected_day 2024-14-03 00:00:00
    busy_times = Proposal.objects.filter(type=doctor, visit_time__gte=selected_day).values_list('visit_time', flat=True)

    selected_week_day = week_days_name[selected_day.weekday()]
    schedule = get_object_or_404(WorkDaysSchedule, doctor=doctor, day__date=selected_week_day)

    start_time = schedule.schedule.datetime_start
    end_time = schedule.schedule.datetime_end

    start_time = datetime.combine(selected_day.date(), start_time, tzinfo=timezone.utc)
    end_time = datetime.combine(selected_day.date(), end_time, tzinfo=timezone.utc)


    # Генерируем слоты и исключаем те которые уже заняты
    intervals = count_intervals(start_time, end_time)
    all_times = [generate_time(start_time, i) for i in range(intervals)]

    available_time_slots = [time for time in all_times if time not in busy_times]
    return available_time_slots


def get_dates_list(today, week_days):
    days = []
    for i in range(14):
        candidate_day: datetime = today + timedelta(days=i)

        verbose_day = week_days_name[candidate_day.weekday()]

        if verbose_day in week_days:
            days.append(candidate_day)
    return days


def proposal(request, doctor_id):
    doctor = get_object_or_404(Post, pk=doctor_id)
    proposals = Proposal.objects.filter(user=request.user, type=doctor)

    if request.method == 'POST':
        form = ProposalForm(data=request.POST)
        if form.is_valid():
            selected_time = form.cleaned_data['selected_time']
            selected_day = form.cleaned_data['selected_day']

            proposal = form.save(commit=False)
            proposal.user = request.user
            proposal.type = doctor
            proposal.visit_time = datetime.combine(selected_day.date(), selected_time)
            proposal.save()

            return redirect(reverse('proposal', args=(doctor_id,)))
        else:
            selected_day = None
    else:
        # Отображение формы для выбора дня и времени записи
        if request.GET.get('selected_day'):
            selected_day = datetime.fromisoformat(request.GET.get('selected_day'))
        else:
            selected_day = None

        form = ProposalForm(selected_day=selected_day)

    # доступные временные слоты для бронирования
    available_time_slots = get_available_time_slots(doctor, request.user, selected_day)
    #  извлекаем временные слоты, которые уже заняты пользователем
    busy_times = Proposal.objects.filter(type=doctor, visit_time__in=available_time_slots, user=request.user).values_list('visit_time', flat=True)

    work_days = Days.objects.filter(wds__doctor=doctor)

    '''
    Берём каждый объект из work_days, получаем из него date (через d.date)
    и кладём в новый список
    '''
    work_days = list(map(lambda d: d.date, work_days))
    today = datetime.today()

    # Получаем рабочие дни на две недели вперёд
    days = get_dates_list(today, work_days)

    context = {'form': form, 'user': request.user, 'time_slots': available_time_slots, 'proposals': proposals, 'busy_times': busy_times, 'days': days, 'selected_day': selected_day}
    return render(request, 'proposal.html', context)


@user_passes_test(lambda user: user.is_authenticated and user.is_moderator)
def change_proposal(request, proposal_id):
    proposal = get_object_or_404(Proposal, id=proposal_id)

    if request.method == 'POST':

        new_status = request.POST.get('status')
        proposal.status = new_status
        proposal.save()

    return render(request, 'change_proposal.html', {'proposal': proposal})


@user_passes_test(lambda user: user.is_authenticated and user.is_moderator)
def all_proposals(request):
    proposals = Proposal.objects.all()
    return render(request, 'all_proposals.html', {'proposals': proposals})
