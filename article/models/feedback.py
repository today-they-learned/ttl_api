from django.db import models
from article.models import Article
from user.models import User


class Feedback(models.Model):
    """Model definition for Feedback"""
    CATEGORY_CHOICES = (
    ('thumbs_up','thumbs_up'),
    ('heart','heart'),
    ('clap','clap'),
    ('lion','lion'),
    ('thinking','thinking'),
    ('smile','smile'),
    ('clover','clover'),
    ('eyes','eyes'),
    ('perfect','perfect'),
    ('bulb','bulb')
)
    
    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE,
        related_name="feedbacks"
    )
    created_at = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name="feedbacks"    
    )
    category = models.CharField(
        null=True,
        choices=CATEGORY_CHOICES,
        max_length=10
    )
    
    class Meta:
        verbose_name="Feedback"
        verbose_name_plural="Feedbacks"
        db_table="feedbacks"