from django.db import models
from user.models import User
from article.models import Article

class Bookmark(models.Model):
    """Model definition for Bookmark"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "bookmarks",
    )
    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE,
        related_name="bookmarks"
    )
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Bookmark"
        verbose_name_plural = "Bookmarks"
        db_table="bookmarks"
