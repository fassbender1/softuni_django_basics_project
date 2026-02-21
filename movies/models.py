from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from common.choices import GenreChoices, MovieStatusChoices
from people.models import Actor, Director, Writer
from studios.models import Studio


# Create your models here.

class Movie(models.Model):

    title = models.CharField(
        max_length=30
    )

    genre = models.CharField(
        max_length=15,
        choices=GenreChoices.choices,
        default="OTHER",
        null=False,
        blank=False,
    )

    movie_poster_image = models.ImageField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    release_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    budget = models.IntegerField(
        null=False,
        blank=False,
    )

    duration = models.IntegerField(
        null=False,
        blank=False,
        default=0,
    )

    status = models.CharField(
        max_length=15,
        choices=MovieStatusChoices.choices,
        default="Other",
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
        default="",
    )

    actors = models.ManyToManyField(
        "people.Actor",
        related_name="movies",
        blank=True,
    )

    directors = models.ManyToManyField(
        "people.Director",
        related_name="movies",
        blank=True,
    )

    writers = models.ManyToManyField(
        "people.Writer",
        related_name="movies",
        blank=True,
    )

    studio = models.ForeignKey(
        Studio,
        related_name="movies",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.genre}")
        super().save(*args, **kwargs)
