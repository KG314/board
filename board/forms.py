from django import forms
from .models import Post, Topic, User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('content', 'image_upload')

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ('topic_name', 'first_post', )

