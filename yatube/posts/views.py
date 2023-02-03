from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


POSTS_PER_PAGE: int = 10

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

def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    context = {
    }
    return render(request, 'posts/post_detail.html', context)
