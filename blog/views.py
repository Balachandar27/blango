from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from django.utils import timezone
from blog.forms import CommentForm
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
from django.http import HttpResponse
import logging

def post_table(request):
    return render(request, "blog/post-table.html")
    
# Create your views here.
# @cache_page(300)
# @vary_on_cookie
def index(request):
    logger = logging.getLogger(__name__)
    # return HttpResponse(str(request.user).encode("ascii"))
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request, "blog/post-detail.html", {"post": post, "comment_form": comment_form})
