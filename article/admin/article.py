from django.contrib import admin
from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin View for Article"""

    list_display = (
        "title",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "user",
    )
    search_fields = ("title",)
    ordering = (
        "created_at",
        "updated_at",
    )
