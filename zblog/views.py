from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from django.http import Http404
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    #1. pass
    #2. return render(request, 'zblog/post_list.html', {})
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('-published_date')

    return render(request, 'zblog/post_list.html', {
        'post_list':qs
    })

def post_detail(request, pk):
    #pass
    qs = get_object_or_404(Post, pk=pk)
    # try:
    #      qs = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    return render(request, 'zblog/post_detail.html', {
        'post':qs,
     })


#@login_required
def post_new(request):
    #pass
    # request.POST, request.FILES
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'zblog/post_edit.html', {
        'form': form
    })



def post_edit(request, pk):
    #pass
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'zblog/post_edit.html', {
        'form': form
    })
