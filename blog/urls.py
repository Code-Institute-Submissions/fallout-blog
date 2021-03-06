from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView, name='homepage'),
    path('news/', views.NewsPage, name="news"),
    path('search/', views.SearchView, name='saerch_view'),
    path('<slug:post>/', views.Post_View, name='post_view'),
    path('category/<category>', views.CategoryView.as_view(), name='category'),

]
