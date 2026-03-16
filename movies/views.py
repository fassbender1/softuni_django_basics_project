from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.choices import MovieStatusChoices
from common.mixins import SearchMixin
from movies.forms import MovieForm, MovieDeleteForm
from movies.models import Movie


# Create your views here.

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/add-movie.html"
    # success_url = reverse_lazy("common:home")

    def form_valid(self, form):
        messages.success(self.request, 'Movie added successfully')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "movies:detail-movie",
            kwargs={"slug": self.object.slug}
        )

class MovieEditView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/edit-movie.html"
    # success_url = reverse_lazy("common:home")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse(
            "movies:detail-movie",
            kwargs={"slug": self.object.slug}
        )

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

class MovieListView(SearchMixin, ListView):
    model = Movie
    paginate_by = 6
    ordering = 'budget'
    template_name = 'movies/movie-list.html'
    model_search_field = "title"

    def get_queryset(self):
        # queryset = Movie.objects.all()
        queryset = super().get_queryset()

        status = self.request.GET.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by("-release_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_status"] = self.request.GET.get("status", "")
        context["status_choices"] = MovieStatusChoices.choices
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie-details.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    http_method_names = ['get']

class HighestBudgetMoviesView(ListView):
    model = Movie
    template_name = "movies/highest-budget.html"
    context_object_name = "movies"
    paginate_by = 5  #

    def get_queryset(self):
        return Movie.objects.all().order_by('-budget')[:5]


