
from django.db import models
from django.utils.text import slugify

from people.validator import agent_validate_email_domain


# Create your models here.

class Person(models.Model):
    name = models.CharField(
        max_length=30
    )

    salary = models.IntegerField(
        blank=True,
        null=True,
    )

    person_profile_image_file = models.ImageField(
        null=True,
        blank=True
    )

    oscar_winner = models.BooleanField(
        blank=True,
        null=True,
        verbose_name="Academy Award Winner",
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

class Actor(Person):

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Birth Date",
    )

    nationality = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Nationality",
    )

    agent_email = models.EmailField(
        unique=True,
        validators=[agent_validate_email_domain],
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Director(Person):

    def __str__(self):
        return self.name


class Writer(Person):

    def __str__(self):
        return self.name