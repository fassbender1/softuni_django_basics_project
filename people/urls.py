from django.urls import path, include

from people import views

app_name = 'people'

urlpatterns = [
    path('', views.CastAndCrewView.as_view(), name='cast-and-crew'),

    # Actors
    path('actors/', views.ActorListView.as_view(), name='actors-list'),
    path('actors/highest-paid/', views.TopPaidActorsView.as_view(), name='highest-paid-actors'),
    path('actors/create/', views.ActorCreateView.as_view(), name='actor-create'),
    path('actors/<slug:slug>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('actors/<slug:slug>/edit/', views.ActorUpdateView.as_view(), name='actor-update'),
    path('actors/<slug:slug>/delete/', views.ActorDeleteView.as_view(), name='actor-delete'),

    # Directors
    path('directors/', views.DirectorListView.as_view(), name='directors-list'),
    path('directors/create/', views.DirectorCreateView.as_view(), name='director-create'),
    path('directors/<slug:slug>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('directors/<slug:slug>/edit/', views.DirectorEditView.as_view(), name='director-update'),
    path('directors/<slug:slug>/delete/', views.DirectorDeleteView.as_view(), name='director-delete'),

    # Writers
    path('writers/', views.WriterListView.as_view(), name='writers-list'),
    path('writers/create/', views.WriterCreateView.as_view(), name='writer-create'),
    path('writers/<slug:slug>/', views.WriterDetailView.as_view(), name='writer-detail'),
    path('writers/<slug:slug>/edit/', views.WriterEditView.as_view(), name='writer-update'),
    path('writers/<slug:slug>/delete/', views.WriterDeleteView.as_view(), name='writer-delete'),
]

# urlpatterns = [
#     path('', include([
#         path('', views.CastAndCrewView.as_view(), name='cast-and-crew'),
#         path('actors/', include([
#             path('', views.ActorListView.as_view(), name='actors-list'),
#             path('create/', views.ActorCreateView.as_view(), name='create'),
#             path('<slug:slug>/', include([
#                 path('', views.ActorDetailView.as_view(), name='actor-detail'),
#                 path('edit/', views.ActorUpdateView.as_view(), name='actor-update'),
#                 path('delete/', views.ActorDeleteView.as_view(), name='actor-delete'),
#             ]))
#             ])),
#         path('directors/', include([
#             path('', views.DirectorListView.as_view(), name='directors-list'),
#             path('create/', views.DirectorCreateView.as_view(), name='create'),
#             path('<slug:slug>/', include([
#                 path('', views.DirectorDetailView.as_view(), name='director-detail'),
#                 path('edit/', views.DirectorEditView.as_view(), name='director-update'),
#                 path('delete/', views.DirectorDeleteView.as_view(), name='director-delete'),
#             ]))
#             ])),
#         path('writers/', include([
#             path('', views.WriterListView.as_view(), name='writers-list'),
#             path('create/', views.WriterCreateView.as_view(), name='create'),
#             path('<slug:slug>/', include([
#                 path('', views.WriterDetailView.as_view(), name='writer-detail'),
#                 path('edit/', views.WriterEditView.as_view(), name='writer-update'),
#                 path('delete/', views.WriterDeleteView.as_view(), name='writer-delete'),
#             ]))
#             ])),
#         ]))
# ]