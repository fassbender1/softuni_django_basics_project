from django.db import models


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

    def __str__(self):
        return self.name