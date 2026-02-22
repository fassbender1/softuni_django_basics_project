from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from common.mixins import SearchMixin
from movies.models import Movie
from people.forms import ActorForm, DirectorForm, WriterForm
from people.models import Actor, Director, Writer

class CastAndCrewView(TemplateView):
    template_name = "people/cast-and-crew.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['actors'] = Actor.objects.all().order_by('name')
        context['directors'] = Director.objects.all().order_by('name')
        context['writers'] = Writer.objects.all().order_by('name')
        context['total_actors'] = context['actors'].count()
        context['total_directors'] = context['directors'].count()
        context['total_writers'] = context['writers'].count()

        return context

class ActorListView(SearchMixin, ListView):
    model = Actor
    template_name = "people/actor-list.html"
    paginate_by = 6

class ActorDetailView(DetailView):
    model = Actor
    template_name = "people/actor-details.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.all()
        return context

class ActorCreateView(CreateView):
    model = Actor
    form_class = ActorForm
    template_name = "people/add-actor.html"
    # success_url = reverse_lazy("people:actor-create")

    def form_valid(self, form):
        messages.success(self.request, f"Actor {form.instance.name} added successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "people:actor-detail",
            kwargs={"slug": self.object.slug}
        )

class ActorUpdateView(UpdateView):
    model = Actor
    form_class = ActorForm
    template_name = "people/edit-actor.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    # success_url = reverse_lazy("people:actors-list")

    def get_success_url(self):
        return reverse(
            "people:actor-detail",
            kwargs={"slug": self.object.slug}
        )

class ActorDeleteView(DeleteView):
    model = Actor
    template_name = "people/delete-actor.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("people:actors-list")

class TopPaidActorsView(ListView):
    model = Actor
    template_name = "people/highest-paid-actors.html"
    context_object_name = "actors"
    # paginate_by = 5

    def get_queryset(self):
        return Actor.objects.filter(salary__isnull=False).order_by('-salary')[:5]



class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = "people/add-director.html"
    # success_url = reverse_lazy("people:directors-list")

    def form_valid(self, form):
        messages.success(self.request, f"Director '{form.instance.name}' created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "people:director-detail",
            kwargs={"slug": self.object.slug}
        )

class DirectorEditView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = "people/edit-director.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse(
            "people:director-detail",
            kwargs={"slug": self.object.slug}
        )



class DirectorDeleteView(DeleteView):
    model = Director
    template_name = "people/delete-director.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("people:directors-list")


class DirectorListView(SearchMixin, ListView):
    model = Director
    paginate_by = 6
    template_name = "people/list-directors.html"


class DirectorDetailView(DetailView):
    model = Director
    template_name = "people/detail-director.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.all()
        return context



class WriterCreateView(CreateView):
    model = Writer
    form_class = WriterForm
    template_name = "people/add-writer.html"
    # success_url = reverse_lazy("people:writers-list")

    def form_valid(self, form):
        messages.success(self.request, f"Writer '{form.instance.name}' created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "people:writer-detail",
            kwargs={"slug": self.object.slug}
        )

class WriterEditView(UpdateView):
    model = Writer
    form_class = WriterForm
    template_name = "people/edit-writer.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    # success_url = reverse_lazy("people:writers-list")

    def get_success_url(self):
        return reverse(
            "people:writer-detail",
            kwargs={"slug": self.object.slug}
        )


class WriterDeleteView(DeleteView):
    model = Writer
    template_name = "people/delete-Writer.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("people:writers-list")


class WriterListView(SearchMixin, ListView):
    model = Writer
    paginate_by = 6
    template_name = "people/list-writers.html"


class WriterDetailView(DetailView):
    model = Writer
    template_name = "people/detail-writer.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.all()
        return context