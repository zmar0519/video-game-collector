from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games_index, name='games_index'),
  path('games/<int:game_id>', views.games_detail,
  name='games_detail'),
  path('games/create', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), 
  name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(),
  name='games_delete'),
  path('games/<int:game_id>/add_review', views.add_review, name="add_review"),
  path('accounts/signup/', views.signup, name='signup'),
]
