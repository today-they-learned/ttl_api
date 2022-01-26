from django.db import models
from django.utils.translation import ugettext_lazy as _


class SnsAccount(models.Model):
    """AbstractModel definition for SnsUser."""

    username = models.TextField(
        verbose_name=_("sns username"),
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        """Meta definition for SnsAccount."""

        abstract = True
        verbose_name = "SnsAccount"
        verbose_name_plural = "SnsAccounts"
        default_related_name = "sns_account"

    def __str__(self):
        """Unicode representation of SnsAccount."""
        return f"{self.user}: {self.username}"
