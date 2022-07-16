from django.shortcuts import render

def add_post(request):
    return render(request, 'add_post.html')

def home(request):
    return render(request, 'home.html')

def post_detail(request, **kwargs):
    return render(request, 'post_detail.html', kwargs)

def update_post(request, **kwargs):
    return render(request, 'post_update.html', kwargs)
