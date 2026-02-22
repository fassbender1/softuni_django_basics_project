from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = ("ACTION", "Action")
    ADVENTURE = ("ADVENTURE", "Adventure")
    ANIMATION = ("ANIMATION", "Animation")
    COMEDY = ("COMEDY", "Comedy")
    CRIME = ("CRIME", "Crime")
    DRAMA = ("DRAMA", "Drama")
    FANTASY = ("FANTASY", "Fantasy")
    HORROR = ("HORROR", "Horror")
    MYSTERY = ("MYSTERY", "Mystery")
    ROMANCE = ("ROMANCE", "Romance")
    SCI_FI = ("SCI_FI", "Science Fiction")
    THRILLER = ("THRILLER", "Thriller")
    WAR = ("WAR", "War")
    WESTERN = ("WESTERN", "Western")
    DOCUMENTARY = ("DOCUMENTARY", "Documentary")
    OTHER = ("OTHER", "Other")

class MovieStatusChoices(models.TextChoices):
    Pre_Production = ("PRE-PRODUCTION", "Pre-Production")
    Filming = ("FILMING", "Filming")
    Post_Production = ("POST-PRODUCTION", "Post-Production")
    Released = ("RELEASED", "Released")
    Other = ("OTHER", "Other")

