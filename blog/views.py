from django.shortcuts import render, get_object_or_404
from .models import Blog 

def all_blogs(request):
    #    blog=Blog.objects.order_by('-date')[:5] el [:5] es un limite de post de blogs que va a mostrar
    blog_count=Blog.objects.count
    blog=Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blog':blog, 'blog_count':blog_count})

def detail(request, blog_id):
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})