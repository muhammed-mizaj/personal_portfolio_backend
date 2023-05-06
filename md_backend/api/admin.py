from django.contrib import admin
from .models import Project,Stack
from django.contrib.admin import ModelAdmin
from django.db.models import F

admin.site.register(Stack)

def make_projects_visible(modeladmin, request, queryset):
    queryset.update(is_visible=True)

make_projects_visible.short_description = "Set Project Visible"

def update_priority(modeladmin, request, queryset):
        # This action will update the priority field by adding 1 to the current value
        queryset.update(priority=F('priority') + 1)

update_priority.short_description = 'Update priority'

@admin.register(Project)
class PaymentGatewayAdmin(ModelAdmin):
    list_display = ['name', 'priority', 'is_visible']
    actions=[make_projects_visible,update_priority]