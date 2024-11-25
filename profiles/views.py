from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Comment, Post

@login_required
def profile_view(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    comments = Comment.objects.filter(author=request.user).order_by('-created_on')  # Get comments for logged in user
    return render(request, 'profiles/profiles.html', {'comments': comments})

#@login_required
#def profile_view(request):
#    # Retrieve posts authored by the logged-in user
#    user_posts = Post.objects.filter(author=request.user)
#
#    # Retrieve comments made by the logged-in user
#    user_comments = Comment.objects.filter(author=request.user)
#
#    # Prepare context data
#    context = {
#        'posts': user_posts,
#        'comments': user_comments,
#    }
#
#    # Render the template with the context
#    return render(request, 'profiles.html', context)
#
#@login_required
#def user_profile(request, username):
#    user = get_object_or_404(User, username=username)
#    posts = Post.objects.filter(author=user)
#    comments = Comment.objects.filter(author=user)
#
#    # Bundle comments with associated posts
#    comments_with_posts = [(comment, comment.post) for comment in comments]
#
#    return render(request, 'profiles/profiles.html', {
#        'user': user,
#        'comments_with_posts': comments_with_posts,
#        'comments': comments,  # Include the standalone comments
#    })