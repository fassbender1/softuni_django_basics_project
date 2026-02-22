from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from movies.forms import MovieForm, MovieDeleteForm
from movies.models import Movie


# Create your views here.

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/add-movie.html"
    success_url = reverse_lazy("common:home")

    def form_valid(self, form):
        messages.success(self.request, 'Movie added successfully')
        return super().form_valid(form)

class MovieEditView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/edit-movie.html"
    success_url = reverse_lazy("common:home")
    slug_field = "slug"
    slug_url_kwarg = "slug"

class MovieDeleteView(DetailView):
    model = Movie
    queryset = Movie.objects.all()
    template_name = "movies/delete-movie.html"
    success_url = reverse_lazy("common:home")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MovieDeleteForm(instance=self.object)
        context['movie'] = self.object
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return redirect("movies:confirm-delete", slug=self.object.slug)

class MovieDeleteConfirmView(DeleteView):
    model = Movie
    template_name = "movies/movie-delete-confirmation.html"
    success_url = reverse_lazy("common:home")
    slug_field = "slug"
    slug_url_kwarg = "slug"

class MovieListView(ListView):
    model = Movie
    paginate_by = 4
    ordering = 'budget'
    template_name = 'movies/movie-list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie-details.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    http_method_names = ['get']



