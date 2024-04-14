from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages

from .models import *


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
    actions = ['mark_new', 'mark_in_progress', 'mark_closed']

    @admin.action(description='Mark status as New')
    def mark_new(self, request, queryset):
        updated = queryset.update(status='N')
        self.message_user(
            request,
            ngettext(
                "%d bug report was successfully marked as New.",
                "%d bug report were successfully marked as New.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description='Mark status as In Progress')
    def mark_in_progress(self, request, queryset):
        updated = queryset.update(status='I')
        self.message_user(
            request,
            ngettext(
                "%d bug report was successfully marked as In Progress.",
                "%d bug report were successfully marked as In Progress.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description='Mark status as Closed')
    def mark_closed(self, request, queryset):
        updated = queryset.update(status='C')
        self.message_user(
            request,
            ngettext(
                "%d bug report was successfully marked as Closed.",
                "%d bug report were successfully marked as Closed.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


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
