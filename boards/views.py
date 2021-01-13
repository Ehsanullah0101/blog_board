from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import newTopicForm, newPostForm

# Create your views here.


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'board_list': boards})


def board_topics(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    return render(request, 'topics.html', {'board': board})


@login_required
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = newTopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('board_topics', pk=board.pk)
    else:
        form = newTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})


def new_post(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = newPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_post', pk=topic.pk)
    else:
        form = newPostForm()

    return render(request, 'new_post.html', {'board': topic, 'form': form})
