from django import forms
from main.models import Comment, Post, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'