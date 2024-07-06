from django.shortcuts import render, redirect
from .forms import VideoForm, CommentForm, UserForm
from .models import Video_model, Comment, User

def video_list(request):
    videos = Video_model.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = Video_model.objects.get(pk=pk)
    comments = Comment.objects.filter(video=video)
    return render(request, 'video_detail.html', {'video': video, 'comments': comments})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

def add_comment(request, pk):
    video = Video_model.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = UserForm()
    return render(request, 'register_user.html', {'form': form})