from .sns_account import SnsAccount


class InstagramAccount(SnsAccount):
    """Model definition for InstagramAccount."""

    class Meta:
        """Meta definition for InstagramAccount."""

        db_table = "instagram_accounts"
        verbose_name = "InstagramAccount"
        verbose_name_plural = "InstagramAccounts"
        default_related_name = "instagram_account"
