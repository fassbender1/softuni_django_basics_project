from django.urls import path, include

from studios import views

app_name = "studios"
urlpatterns = [
    path('', views.StudioListView.as_view(), name='studio-list'),
    path('create/', views.StudioCreateView.as_view(), name='studio-create'),
    path('<slug:slug>/', include([
        path('', views.StudioDetailView.as_view(), name='studio-detail'),
        path('edit/', views.StudioEditView.as_view(), name='studio-edit'),
        path('delete/', views.StudioDeleteView.as_view(), name='studio-delete'),
        ]))
]