from django.db import models
from django.utils.text import slugify


# Create your models here.

class Studio(models.Model):
    name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        unique=True,
    )

    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    founded_in = models.DateField(
        blank=True,
        null=True,
    )

    studio_head = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name