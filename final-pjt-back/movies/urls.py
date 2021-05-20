from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('create/', views.movie_create),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.comment_create),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/<str:mbti_type>/', views.mbti_set),
]
