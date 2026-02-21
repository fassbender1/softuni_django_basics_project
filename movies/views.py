from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from movies.forms import MovieForm
from movies.models import Movie


# Create your views here.

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/add-movie.html"

