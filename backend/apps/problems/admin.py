"""
Admin configuration for problems app.
"""
from django.contrib import admin

from .models import Problem, Submission


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'created_by', 'created_at']
    list_filter = ['difficulty', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'problem', 'language', 'status', 'submitted_at']
    list_filter = ['status', 'language', 'submitted_at']
    search_fields = ['user__username', 'problem__title']
    ordering = ['-submitted_at']
    readonly_fields = ['submitted_at']
