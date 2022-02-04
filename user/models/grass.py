from django.db import models
from . import User
class Grass(models.Model):
    """Model definition for Grass"""
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "grasses",
        verbose_name="user"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    study_count = models.PositiveIntegerField(
        default=0
    )
    write_count = models.PositiveIntegerField(
        default=0
    )
    edit_count = models.PositiveIntegerField(
        default=0
    )
    class Meta:
        verbose_name="Grass"
        verbose_name_plural="Grasses"
        db_table="grasses"
