from django.shortcuts import render, get_object_or_404
from bikeblog.models import Post, Comment  # Import both Post and Comment here.

def profile_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(approved=True)  # Adjust based on whether you're showing only approved comments
    return render(request, 'profiles.html', {'post': post, 'comments': comments})