from django.db import models
from . import User


class Grass(models.Model):
    """Model definition for Grass"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="grasses", verbose_name="user"
    )
    study_count = models.PositiveIntegerField(default=0)
    write_count = models.PositiveIntegerField(default=0)
    edit_count = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Grass"
        verbose_name_plural = "Grasses"
        db_table = "grasses"
