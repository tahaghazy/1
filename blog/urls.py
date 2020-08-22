from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('most-watched/', views.most_watched, name='most-watched'),
    path('newest/', views.newest, name='newest'),
    path('most-rated/', views.most_rated, name='most-rated'),
    path('type/<slug:slug>/', views.movies, name='movies'),
    path('category/<slug:slug>/', views.secondcategory, name='secondcategory'),
    path('detail/<str:slug>/', views.post_detail, name='detail'),
    path('new_post',views.PostCreateView.as_view(),name='new_post'),
    path('detail/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('detail/<slug:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('searchposts/', views.searchposts, name='searchposts'),

]