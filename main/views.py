from django.shortcuts import redirect, render, get_object_or_404
from main.models import Comment
from .forms import AddPostForm, CommentForm
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




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    image = post.get_image
    images = post.posts.exclude(image=image)
    return render(request, 'post-detail.html', locals())



def add_post(request):
    if request.method == 'POST':
        post_form = AddPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
            return redirect(post.get_absolute_url())

    else:
        post_form = AddPostForm()
    return render(request, 'add_post.html ', locals())


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
