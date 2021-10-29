from django import forms
from django.contrib.postgres import search
from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import NewCommentForm,SearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, query
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def home3(request):
    return render(request, 'blogs/base2.html')


def post_searcher(request):
   
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched is not None:
            searched_post = Post.newmanager.filter(Q (title__icontains=searched) | Q (slug__icontains=searched)) or Post.newmanager. annotate(search=SearchVector( 'category',),).filter(search=searched)
            cnt = searched_post.count() < 1
            print('searched_post are:',searched_post)
            if cnt:
                print('searched_post are:',searched_post)
                none_hai = cnt
                return render(request,'blogs/result.html',{'none':none_hai})

            return render(request,'blogs/result.html',{'posts':searched_post,'query':searched})

    return render(request,'blogs/result.html')

def home(request,by_tags=None,by_category=None):

    all_posts = Post.newmanager.all()
    
    if by_tags is not None:
        posts = Post.objects.filter(tags__name=by_tags)
        return render(request, 'index.html', {'posts': posts})

    if by_category is not None:
        posts = Post.objects.filter(category__name=by_category)
        return render(request, 'index.html', {'posts': posts})
    
    return render(request, 'index.html', {'posts': all_posts})
    # return render(request, 'blogs/design.html', {'posts': all_posts})



def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='published')
    allcomments = post.comments.filter(status=True)
    post_tags_name = post.tags.values_list('id',flat=True)
    similar_posts = Post.newmanager.filter(tags__in=post_tags_name).exclude(id=post.id)[:4]
    print("similar_posts are: ",similar_posts.count())
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    
    context = {
        'post': post,
        'comments':  user_comment,
        'comments': comments, 
        'comment_form': comment_form,
        'allcomments': allcomments,
        'similar_posts':similar_posts,

    }
    return render(request, 'blogs/single2.html',context)
    # return render(request, 'single.html',context)


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context
