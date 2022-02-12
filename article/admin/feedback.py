from django.contrib import admin
from article.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Admin View for Feedback"""

    list_display = (
        "user",
        "article",
        "created_at",
    )
    readonly_fields = ("created_at",)
    ordering = ("created_at",)
