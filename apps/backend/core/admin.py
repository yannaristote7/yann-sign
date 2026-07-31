from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "action",
        "ip_address",
        "created_at",
    )

    list_filter = (
        "action",
        "created_at",
    )

    search_fields = (
        "description",
        "user__username",
    )

    readonly_fields = (
        "user",
        "action",
        "description",
        "ip_address",
        "user_agent",
        "created_at",
    )