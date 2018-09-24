from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Topic, User
from .forms import PostForm, TopicForm
from datetime import datetime
#from django.contrib.auth.models import AnonymousUser

# Create your views here.
def topic_list(request):
    topics = Topic.objects.order_by('-updated_at')
    return render(request, 'topic_list.html', {'topics': topics})

def post_list(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all().order_by('posted_at')
    return render(request, 'post_list.html', {'topic': topic, 'posts': posts})

def new_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            if request.user.is_authenticated():
                post.posted_by = request.user
            post.save()
            topic.updated_at = datetime.now()
            topic.save()
            return redirect('posts', pk=pk)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.updated_at = datetime.now()
            if request.user.is_authenticated():
                topic.created_by = request.user
            topic.save()
            first_post = Post(
                content=topic.first_post,
                topic=topic,
                #posted_by=request.user
            )
            if request.user.is_authenticated():
                first_post.posted_by = request.user
            first_post.save()
            return redirect('posts', pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'new_topic.html', {'form': form})
