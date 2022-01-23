from .sns_account import SnsAccount


class InstagramAccount(SnsAccount):
    """Model definition for InstagramAccount."""

    @staticmethod
    def get_user_related_name():
        return "instgram_account"

    class Meta:
        """Meta definition for InstagramAccount."""

        db_table = "instagram_accounts"
        verbose_name = "InstagramAccount"
        verbose_name_plural = "InstagramAccounts"
