from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from main.models import Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from main.models import Category, Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_template_names(self):
        template_name = super(HomePageView, self).get_template_names()
        search = self.request.GET.get('query')
        if search:
            template_name = 'search.html'
        return template_name


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('query')
        if search:
            context['posts'] = Post.objects.filter(Q(title__icontains=search)|
                                                   Q(description__icontains=search)|
                                                   Q(user__icontains=search))
        else:
            context['posts'] = Post.objects.all()
        return context




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


# comments


def post_list(request):
    post = Post.objects.filter(moder=True)
    return render(request, 'post/post.html', locals())


def one_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
        else:
            form = CommentForm()
        return render(request, 'post/post.html', {"post": post, "form": form, "comment": comment})
