from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.mixins import SearchMixin
from studios.forms import StudioForm
from studios.models import Studio


class StudioCreateView(CreateView):
    model = Studio
    form_class = StudioForm
    template_name = "studios/add-studio.html"
    success_url = reverse_lazy("studios:studio-list")

    def form_valid(self, form):
        messages.success(self.request, f"Studio '{form.instance.name}' created successfully!")
        return super().form_valid(form)


class StudioEditView(UpdateView):
    model = Studio
    form_class = StudioForm
    template_name = "studios/edit-studio.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("studios:studio-list")


class StudioDeleteView(DeleteView):
    model = Studio
    template_name = "studios/delete-studio.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("studios:studio-list")


class StudioListView(SearchMixin, ListView):
    model = Studio
    paginate_by = 6
    template_name = "studios/studio-list.html"


class StudioDetailView(DetailView):
    model = Studio
    template_name = "studios/studio-details.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.object.movies.all()
        return context