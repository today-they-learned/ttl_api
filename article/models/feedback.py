from django.db import models
from user.models import User

CATEGORY_CHOICES = (
    ("thumbs_up", "thumbs_up"),
    ("heart", "heart"),
    ("clap", "clap"),
    ("lion", "lion"),
    ("thinking", "thinking"),
    ("smile", "smile"),
    ("clover", "clover"),
    ("eyes", "eyes"),
    ("perfect", "perfect"),
    ("bulb", "bulb"),
)


class Feedback(models.Model):
    """Model definition for Feedback"""

    article = models.ForeignKey(
        "article.Article", on_delete=models.CASCADE, related_name="feedbacks"
    )
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    category = models.CharField(
        null=False,
        default="thumbs_up",
        choices=CATEGORY_CHOICES,
        max_length=10,
    )

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        db_table = "feedbacks"
