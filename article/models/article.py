from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _


SOURCE_CHOICES = [
    ("tl", "TTL"),
    ("vl", "Velog"),
    ("gh", "Github"),
    ("ts", "Tistory"),
]


class Article(models.Model):
    """Model definition for Article."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name="writer",
    )
    title = models.CharField(
        max_length=50,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    source = models.CharField(
        null=True,
        choices=SOURCE_CHOICES,
        default="tl",
        max_length=2,
    )
    thumbnail = models.ImageField(
        upload_to="article/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # article 레코드가 생성된 일저
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )  # article 레코드가 수정된 일자

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "articles"
