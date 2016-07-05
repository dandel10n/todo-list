from django.contrib import admin
from .models import Task

def make_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)
make_completed.short_description = "Mark selected tasks as completed"

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('due_date',)
    actions = [make_completed]
    list_display = ('title', 'due_date', 'is_completed')
    search_fields = ['title']

admin.site.register(Task, TaskAdmin)
