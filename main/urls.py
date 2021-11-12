from django.urls import path

from main.views import CategoryDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    
]