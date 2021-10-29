from django import template
from django.contrib.postgres import search
from django.http import request
from blog import forms
from blog.models import Post,Category
from django.db.models import Q 
from blog.forms import SearchForm
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

register = template.Library()

@register.simple_tag
def total_post():
    total_post = Post.newmanager.count() 

    context = {
        'total_post':total_post,
    }
    return total_post

@register.simple_tag
def get_most_commented_post(count=3):
    most_commented = Post.newmanager.annotate(total_comments=count('comments')).order_by('-total_comments')[:3]
    return {'most_comment_post':most_commented}


@register.inclusion_tag('blogs/latest_post.html')
def show_latest_post(count=4):
    latest_post = Post.newmanager.order_by('-publish')[:count]
    return {'latest_post':latest_post}

@register.inclusion_tag('blogs/category.html')
def by_category():
    all_category = Category.objects.all()
    print('all_category:',all_category)
    return {'all_category':all_category}

@register.inclusion_tag('blogs/tags.html')
def show_by_tags():
    all_tags = Post.tags.all()
    return {'all_tags':all_tags}

@register.inclusion_tag('blogs/cats.html')
def my_cats():
    category = 1
    cats_count = Post.objects.filter(category_id=category).count()
    return {'cats_count':cats_count}

