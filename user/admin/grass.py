from django.contrib import admin
from user.models import Grass


@admin.register(Grass)
class GrassAdmin(admin.ModelAdmin):
    """Admin View for Grass"""

    readonly_fields = ("created_at",)
    ordering = ("created_at",)
