from django.urls import path

from movies import views

app_name = 'movies'
urlpatterns = [
    path('create-movie/', views.MovieCreateView.as_view(), name='create-movie'),

]