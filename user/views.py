from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.models import User
from user.forms import RegisterForm, LoginForm, ProfileForm
from article.models import Article
from django.core.paginator import Paginator
from django.db.models import Q
import markdown

# Create your views here.


def profile(request, username):
    error = ''
    user = User.objects.get(username=username)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        avatar = request.FILES.get('avatar')
        if 'avatar' in request.FILES:
            user.avatar = avatar
            user.save()
            request.session['user_avatar_url'] = user.avatar.url
        print("???")
        if profile_form.is_valid():
            user.username = profile_form.cleaned_data.get('username')
            user.email = profile_form.cleaned_data.get('email')
            user.biography = profile_form.cleaned_data.get('biography')
            print("OK1")
            user.save()
            # error = 'update successfully'
            return render(request, 'user/profile.html', locals())
        print(profile_form.errors)
    return render(request, 'user/profile.html', locals())

    # user = User.objects.get(id=id)
    # profile = Profile.objects.get(user_id=id)
    # if request.method == 'POST':
    #     if request.user != user:
    #         return HttpResponse('You have no permission to change it')
    #     profile_form = ProfileForm(request.POST)
    #     if profile_form.is_valid():
    #         profile.biography = profile_form.cleaned_data.get('biography')
    #         profile.save()
    #         return redirect('/user/profile_update', username=user.username)
    #     else:
    #         return HttpResponse("注册表单输入有误。请重新输入:(")
    # return render(request, 'user/profile.html', locals())


def user_logout(request):
    logout(request)
    return redirect('/user/login')


def user_login(request):
    # error = ''
    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     if user_form.is_valid():
    #         username = user_form.cleaned_data.get('username')
    #         password = user_form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             login(request, user)
    #             return redirect('/user/homepage')
    #         else:
    #             error = '账号或密码输入有误。请重新输入:('
    #             return render(request, 'user/login.html', locals())
    #     else:
    #         error = 'nmsl'
    # return render(request, 'user/login.html', locals())

    error = ''
    if request.session.get('flag_register'):
        if request.session.get('flag_register2'):
            request.session['flag_register'] = False
            request.session['flag_register2'] = False
        else:
            request.session['flag_register2'] = True
    if request.session.get('is_login'):
        try:
            User.objects.get(id=request.session.get('user_id'))
            return redirect('user:homepage')
        except User.DoesNotExist:
            request.session.flush()
    if request.method == 'POST':
        user_form = LoginForm(data=request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            try:
                exist_user = User.objects.get(username=username)
            except User.DoesNotExist:
                error = 'Your username does not exist'
                return render(request, 'user/login.html', locals())
            finally:
                pass
            if password == exist_user.password:
                request.session['is_login'] = True
                request.session['user_id'] = exist_user.id
                request.session['user_name'] = exist_user.username
                if exist_user.avatar:
                    request.session['user_avatar_url'] = exist_user.avatar.url
                return redirect('/user/homepage/')
            else:
                error = 'Your password does not match!'
                return render(request, 'user/login.html', locals())
    return render(request, 'user/login.html', locals())


def user_register(request):
    # error = ''
    # if request.method == 'POST':
    #     user_form = RegisterForm(data=request.POST)
    #     if user_form.is_valid():
    #         password1 = user_form.cleaned_data.get('password')
    #         password2 = user_form.cleaned_data.get('password2')
    #         if password1 == password2:
    #             new_user = user_form.save(commit=False)
    #             new_user.set_password(password1)
    #             new_user.save()
    #             request.session['register_success'] = True
    #             return redirect('/user/login')
    #         else:
    #             error = '两次输入的密码不一致'
    #             return render(request, 'user/register.html', locals())
    # return render(request, 'user/register.html', locals())

    error = ''
    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)
        if user_form.is_valid():
            new_user = User()
            print(user_form.cleaned_data)
            new_username = user_form.cleaned_data.get('username')
            new_email = user_form.cleaned_data.get('email')
            if User.objects.filter(username=new_username):
                error = 'The username has been registered'
                return render(request, 'user/register.html', locals())
            elif new_email != '' and User.objects.filter(email=new_email):
                error = 'The email has been registered'
                return render(request, 'user/register.html', locals())
            password1 = user_form.cleaned_data.get('password')
            password2 = user_form.cleaned_data.get('password2')
            if password1 != password2:
                error = 'Your password dose not match'
                return render(request, 'user/register.html', locals())
            new_user.username = new_username
            new_user.password = password1
            new_user.email = new_email
            new_user.save()
            request.session['flag_register'] = True
            return redirect('/user/login/')
        error = 'please complete the form!'
    return render(request, 'user/register.html', locals())


def homepage(request):
    article_list = Article.objects.all()
    search = request.GET.get('search')
    order = request.GET.get('order')
    if not search: search = ''
    if search:
        article_list = Article.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')
    # user = User.objects.get(id=request.session.get('user_id'))
    # if request.GET.get('order') == 'total_views':
    #     article_list = Article.objects.all().order_by('-total_views')
    #     order = 'total_views'
    # else:
    #     article_list = Article.objects.all()
    #     order = 'normal'
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # for article in articles:
    #     article.content = markdown.markdown(article.content,
    #                                         extensions=['markdown.extensions.extra',
    #                                                     'markdown.extensions.codehilite', ])

    # if request.session.get('is_login'):
    #     request.session['user_avatar_url'] =\
    #         User.objects.get(id=request.session.get('user_id')).avatar.url
    flag_homepage = True
    return render(request, 'user/homepage.html', locals())


def nashi(request):
    return redirect('user:login')
