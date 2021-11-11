from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Category, Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'detail_list.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category_id=self.slug)
        return context


