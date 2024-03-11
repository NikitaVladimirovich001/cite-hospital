from django.shortcuts import render, get_object_or_404, redirect
from glav.forms import CommentForm
from glav.models import Post
from proposal.models import WorkDaysSchedule, Proposal


def index(request):    # Главная
    return render(request, 'index.html')


def post(request):  # Врачи
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})


def about(request):  # О врачах
    about = Post.objects.all()
    return render(request, 'about.html', {'about': about})


def timeslot(request):  # Расписание
    timeslot = WorkDaysSchedule.objects.all()
    return render(request, 'timeslot.html', {'timeslot': timeslot})

def kabinet(request):  # Кабинет
    kabinet = Proposal.objects.filter(user=request.user)
    return render(request, 'kabinet.html', {'kabinet': kabinet})

def comment(request, post_id):  # Комментарии
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('comment', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'post': post, 'comments': comments, 'form': form})