from django.shortcuts import render, redirect
from comment.form import CommentForm
from comment.models import Comment
from user.models import User
from article.models import Article
from django.http import HttpResponse

# Create your views here.


def comment_post(request, article_id):
    error = ''
    if not request.session.get('is_login'):
        error = '登录后才能评论哦:)'
        return redirect('article:article_detail', article_id)
    user = User.objects.get(username=request.session.get('user_name'))
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = user
            new_comment.article = article
            new_comment.save()
            user.comment_reply += 1
            user.save()
            article.comments += 1
            article.save()
            return redirect('article:article_detail', article_id=article_id)
    return HttpResponse('nmsl zaizhong')
