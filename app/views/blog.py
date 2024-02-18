from django.shortcuts import redirect, render, get_object_or_404

from app.forms import SubscribeForm, BookingModelForm, BlogCommentForm
from app.models.blog import Blog, BlogComment
from app.models.other import MainSocialNetwork


def blog_view(request):
    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        if form_type == 'formOne':
            form = SubscribeForm(request.POST)
        elif form_type == 'formTwo':
            form = BookingModelForm(request.POST)
        else:
            # Default to SubscribeForm if form_type is not specified or unrecognized
            form = SubscribeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    # Default to SubscribeForm if it's a GET request or form_type is not specified
    form = SubscribeForm()
    social_networks = MainSocialNetwork.objects.all()
    popular_blogs = Blog.objects.order_by('-created_at')[:2]
    latest_blogs = Blog.objects.order_by("-created_at")[:6]
    publications = Blog.objects.order_by("-created_at")[:3]
    return render(request, 'app/blog.html',
                  {'social_networks': social_networks,
                   "popular_blogs": popular_blogs,
                   "latest_blogs": latest_blogs,
                   "publications": publications,
                   "form": form})


def publication_view(request, blog_id):
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "formOne":
            form = BlogCommentForm(request.POST)
        elif form_type == "formTwo":
            form = BookingModelForm(request.POST)
        else:
            # Default to BlogCommentForm if form_type is not specified or unrecognized
            form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = get_object_or_404(klass=Blog, id=blog_id)
            comment.save()
            return redirect('index')

    form = BlogCommentForm()
    social_networks = MainSocialNetwork.objects.all()
    blog = get_object_or_404(klass=Blog, id=blog_id)
    comments = BlogComment.objects.filter(blog_id=blog_id).order_by('-created_at')[:3]
    comments_count = BlogComment.objects.filter(blog_id=blog_id).count()
    blogs = Blog.objects.all()

    return render(request, 'app/publication.html',
                  {'social_networks': social_networks,
                   "blog": blog,
                   "blogs": blogs,
                   "form": form,
                   "comments": comments,
                   "comments_count": comments_count})
