from django.urls import path

from main.views import CategoryDetailView, HomePageView, add_post, post_detail

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    path('post-detail/<int:pk>/', post_detail, name='post-detail'),
    path('add-post/', add_post, name='add-post')
]