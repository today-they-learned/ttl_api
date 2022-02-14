from django.db import models


class UploadImage(models.Model):
    """Model definition for UploadImage."""

    image = models.ImageField(
        upload_to="uploads/",
        blank=True,
        null=True,
    )

    class Meta:
        """Meta definition for UploadImage."""

        verbose_name = "UploadImage"
        verbose_name_plural = "UploadImages"
        db_table = "upload_images"
