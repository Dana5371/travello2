from django import forms
from main.models import Comment, Image, Post
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'comment')

    widgets = {
        'user': forms.TextInput(attrs={'class': 'form-control'}),
        'comment': forms.Textarea(attrs={'class': 'form-control'})
    }


class AddPostForm(forms.ModelForm):
    created = forms.DateField(initial=datetime.now().strftime('%Y-%m-%d'))
    class Meta:
        model = Post
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )