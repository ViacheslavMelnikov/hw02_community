from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница Последние обновления на сайте
    path('', views.index, name='index'),
    # Все посты указанной группы
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
