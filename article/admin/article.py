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
    )
    search_fields = ("title",)
    ordering = (
        "created_at",
        "updated_at",
    )
    actions = [
        "reset_bookmark_count",
        "reset_feedback_count",
        "reset_study_count",
        "reset_score",
    ]

    @admin.action(description="study count 초기화")
    def reset_study_count(modeladmin, request, queryset):
        articles = queryset

        for article in articles:
            article.reset_study_count()

    @admin.action(description="feedback count 초기화")
    def reset_feedback_count(modeladmin, request, queryset):
        articles = queryset

        for article in articles:
            article.reset_feedback_count()

    @admin.action(description="bookmark count 초기화")
    def reset_bookmark_count(modeladmin, request, queryset):
        articles = queryset

        for article in articles:
            article.reset_bookmark_count()

    @admin.action(description="score 초기화")
    def reset_score(modeladmin, request, queryset):
        articles = queryset

        for article in articles:
            article.reset_score()
