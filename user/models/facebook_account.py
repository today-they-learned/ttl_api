from .sns_account import SnsAccount


class FacebookAccount(SnsAccount):
    """Model definition for FacebookAccount."""

    @staticmethod
    def get_user_related_name():
        return "facebook_account"

    class Meta:
        """Meta definition for FacebookAccount."""

        db_table = "facebook_accounts"
        verbose_name = "FacebookAccount"
        verbose_name_plural = "FacebookAccounts"
