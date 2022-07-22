from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'blog_website/index.html', context=context)


def listing_page(request):
    context = {
        'title': 'Listing',
    }
    return render(request, 'blog_website/listing.html', context=context)


def post_page(request):
    context = {
        'title': 'Post',
    }
    return render(request, 'blog_website/post.html', context=context)


def test_page(request):
    context = {
        'title': 'Test',
    }
    return render(request, 'blog_website/test.html', context=context)
