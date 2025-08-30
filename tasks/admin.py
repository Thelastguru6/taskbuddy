from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',  'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')

admin.site.site_header = "TaskBuddy Admin"
admin.site.site_title = "TaskBuddy Admin Portal"
admin.site.index_title = "Welcome to TaskBuddy Admin Portal"
