from django.shortcuts import render, redirect
from article.models import Article
from article.forms import ArticleForm
from user.models import User
from comment.models import Comment
import markdown

# Create your views here.


def article_modify(request, username, article_id):
    error = ''
    article = Article.objects.get(id=article_id)
    user = User.objects.get(username=username)
    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article.title = article_form.cleaned_data.get('title')
            article.content = article_form.cleaned_data.get('content')
            article.save()
            return redirect('article:article_detail', article_id=article_id)
    return render(request, 'article/article_modify.html', locals())


def article_delete(request, user_id, article_id):
    error = ''
    article = Article.objects.get(id=article_id)
    user = User.objects.get(id=user_id)
    if user_id == article.author_id:
        article.delete()
        return redirect('user:homepage')
    error = 'nmsl???'
    pass


def article_post(request, username):
    error = ''
    user = User.objects.get(username=username)
    if request.method == 'POST':
        post_form = ArticleForm(data=request.POST)
        if post_form.is_valid():
            author = User.objects.get(username=username)
            new_article = post_form.save(commit=False)
            new_article.author = author
            # new_article.content = markdown.markdown(new_article.content,
            #                                     extensions=['markdown.extensions.extra',
            #                                                 'markdown.extensions.codehilite', ])
            new_article.save()
            author.article_posted += 1
            # return redirect('/user/homepage/')
            return redirect('user:homepage')
        else:
            error = '你输入的信息有误，请重新输入'
            return render(request, 'article/article_post.html', locals())
    post_form = ArticleForm()
    username = request.session.get('user_name')
    return render(request, 'article/article_post.html', locals())


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    article.content = markdown.markdown(article.content,
                                        extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', ])
    comments = Comment.objects.all()
    if article.author_id != request.session.get('user_id'):
        article.total_views += 1
        article.save(update_fields=['total_views'])
    return render(request, 'article/article_detail.html', locals())
