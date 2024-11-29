from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment, Post


@login_required
def profile_view(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    """ Get comments for logged in user """
    comments = Comment.objects.filter(author=request.user).order_by('-created_on')
    return render(request, 'profiles/profiles.html', {'comments': comments})
