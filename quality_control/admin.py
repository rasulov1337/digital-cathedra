from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at',
                    'updated_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    list_filter = ('status', 'priority', 'created_at', 'updated_at')
    fieldsets = [
        (
            None,
            {
                'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
            }
        )
    ]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'task', 'priority', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    fieldsets = [
        (
            None,
            {
                'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
            }
        )
    ]
