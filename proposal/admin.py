from django.contrib import admin
from .models import Post, Proposal, WorkDaysSchedule, Days, WorkSchedule


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'fio', 'experience', 'category', 'phone_number')
    search_fields = ('name', 'fio', 'phone_number')
    ordering = ('name',)

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'status', 'created_at', 'updated_at', 'visit_time')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__name', 'user__surname', 'user__email', 'type__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(WorkDaysSchedule)
class WorkDaysScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'doctor', 'schedule')
    list_filter = ('day', 'doctor', 'schedule')
    search_fields = ('doctor__name',)

@admin.register(Days)
class DaysAdmin(admin.ModelAdmin):
    exclude = []

@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    exclude = []