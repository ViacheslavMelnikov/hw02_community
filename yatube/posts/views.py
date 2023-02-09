from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group, User
from .forms import PostForm
from .constants import POSTS_PER_PAGE


@login_required
def index(request):
    # post_list = Post.objects.all().order_by('-pub_date')
    # Если порядок сортировки определен в классе Meta модели,
    # запрос будет выглядеть так:
    post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list,POSTS_PER_PAGE)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }

    # Было до Паджинатора
    # posts = Post.objects.all()[:POSTS_PER_PAGE]
    # В словаре context отправляем информацию в шаблон
    # context = {'posts': posts, }
    return render(request, 'posts/index.html', context)

@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group)
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list,POSTS_PER_PAGE)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {'group': group, 
        'page_obj': page_obj,
    }


    # Было до Паджинатора

    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    # group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    # posts = Post.objects.filter(group=group)[:POSTS_PER_PAGE]
    # context = {'group': group, 'posts': posts, }
    return render(request, 'posts/group_list.html', context)

@login_required
def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts=Post.objects.filter(author_id=author)
    post_count=posts.count()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author, 
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj, 
        'post_count':post_count,
        'posts':posts,
    }

    return render(request, 'posts/profile.html', context)

@login_required
def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, pk=post_id)
    post_count=Post.objects.filter(author_id=post.author.pk).count()
    context = {
        'post':post,
        'post_count':post_count
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    is_edit=False
    is_title="Добавить запись"
    is_but_txt="Добавить"
    form=PostForm()
    groups=Group.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('posts:profile',request.user.username)
        data={
        'form':form,
        'groups':groups,
        'is_edit':is_edit,
        'is_title':is_title,
        'is_but_txt':is_but_txt
        }
        return render(request,'posts/post_create.html', data)

    data={
        'form':form,
        'groups':groups,
        'is_edit':is_edit,
        'is_title':is_title,
        'is_but_txt':is_but_txt
        }
    return render(request,'posts/post_create.html',data)

@login_required
def post_edit(request, post_id):
    is_edit=True
    is_title="Редактировать запись"
    is_but_txt="Сохранить"
    post = get_object_or_404(Post, pk=post_id)
    author=post.author
    groups=Group.objects.all()
    form=PostForm(request.POST,instance=post)
    if request.user == author:
        if request.method=='POST' and form.is_valid():
            post=form.save()
            return redirect('posts:post_detail', post_id)
    
        is_edit=True
        context={'form':form,
            'groups':groups,
            'post':post,
            'is_edit':is_edit,
            'is_title':is_title,
            'is_but_txt':is_but_txt,
            }
        return render(request,'posts/post_create.html', context )
    return redirect('posts:post_detail', post_id)
