from common.forms import SearchForm


# class SearchMixin:
#     search_param = 'search_name'
#     search_form_class = SearchForm
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.search_form = self.search_form_class(self.request.GET or None)
#         if self.search_form.is_valid():
#             search_value = self.search_form.cleaned_data.get(self.search_param)
#             if search_value:
#                 queryset = queryset.filter(name__icontains=search_value)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.search_form
#         return context

class SearchMixin:
    search_field = 'search_name'
    model_search_field = 'name'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get(self.search_field, '').strip()
        if query:
            filter_kwargs = {f"{self.model_search_field}__icontains": query}
            queryset = queryset.filter(**filter_kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context