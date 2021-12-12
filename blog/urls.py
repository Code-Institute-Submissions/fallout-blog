from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView, name='homepage'),
    path('<slug:post>/', views.Post_View, name='post_view'),
    path('category/<category>', views.CategoryView.as_view(), name='category'),
]
