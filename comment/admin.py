from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = (
        "user",
        "article",
    )
