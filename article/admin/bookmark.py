from django.contrib import admin
from article.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """Admin View for Bookmark"""

    list_display = (
        "user",
        "article",
        "created_at",
    )
    readonly_fields = ("created_at",)
    ordering = ("created_at",)
