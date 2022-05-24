from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, blogUpdateView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', blogUpdateView.as_view(), name='post_edit'),
    path('', BlogListView.as_view(), name='home'),
    path('post_new/', BlogCreateView.as_view(), name='new_post')
]
