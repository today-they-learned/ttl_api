from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


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
    )  # Article 작성자
    title = models.CharField(
        max_length=50,
    )  # 제목
    content = models.TextField(
        null=True,
        blank=True,
    )  # 내용
    tags = TaggableManager(
        blank=True,
    )  # 태그
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
    study_count = models.PositiveIntegerField(
        default=0,
    )  # 조회수
    feedback_count = models.PositiveIntegerField(
        default=0,
    )  # 받은 피드백 수
    score = models.IntegerField(
        verbose_name=_("score"),
        default=0,
    )  # 인기순
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # article 레코드가 생성된 일자
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

    def increment_study_count(self):
        self.study_count += 1
        self.save()
        self.reset_score()

    def increment_feedback_count(self):
        self.feedback_count += 1
        self.save()
        self.reset_score()

    def decrement_feedback_count(self):
        self.feedback_count -= 1
        self.save()
        self.reset_score()

    def reset_score(self):
        self.score = self.study_count + self.feedback_count * 15
        self.save()
