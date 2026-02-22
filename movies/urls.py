from django.urls import path, include

from movies import views

app_name = 'movies'
urlpatterns = [
    path('', views.MovieListView.as_view(), name='list-movies'),
    path('highest-budget/', views.HighestBudgetMoviesView.as_view(), name='highest-budget'),
    path('create-movie/', views.MovieCreateView.as_view(), name='create-movie'),
    path('<slug:slug>/', include([
        path('', views.MovieDetailView.as_view(), name = 'detail-movie'),
        path('edit/', views.MovieEditView.as_view(), name='edit-movie'),
        path('delete/', include([
            path('', views.MovieDeleteView.as_view(), name='delete-movie'),
            path('confirm/', views.MovieDeleteConfirmView.as_view(), name='confirm-delete'),
            ]))

    ]))

]