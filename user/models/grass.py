from django.db import models
from . import User
from django.utils.timezone import now


class Grass(models.Model):
    """Model definition for Grass"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="grasses", verbose_name="user"
    )
    study_count = models.PositiveIntegerField(default=0)
    write_count = models.PositiveIntegerField(default=0)
    edit_count = models.PositiveIntegerField(default=0)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Grass"
        verbose_name_plural = "Grasses"
        db_table = "grasses"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "created_at"], name="user_created_at_unique_index"
            )
        ]

    @classmethod
    def increment_study_count(cls, user):
        grass, _ = cls.objects.get_or_create(
            user=user,
            created_at=now(),
        )
        grass.study_count += 1

        grass.save()

    @classmethod
    def increment_write_count(cls, user):
        grass, _ = cls.objects.get_or_create(
            user=user,
            created_at=now(),
        )
        grass.write_count += 1

        grass.save()

    @classmethod
    def increment_edit_count(cls, user):
        grass, _ = cls.objects.get_or_create(
            user=user,
            created_at=now(),
        )
        grass.edit_count += 1

        grass.save()
