from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


POSTS_PER_PAGE: int = 10


def index(request):
    title = ''
    posts = Post.objects.all()[:POSTS_PER_PAGE]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    title = ''
    posts = Post.objects.filter(group=group)[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
