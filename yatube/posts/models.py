from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # название группы
    title = models.CharField(max_length=200)
    # уникальный адрес группы, часть URL
    # (например, для группы любителей котиков
    # slug будет равен cats: group/cats)
    slug = models.SlugField(unique=True)
    # текст, описывающий сообщество.
    # Этот текст будет отображаться на странице сообщества
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # Ссылка на модель Group
    # Параметр on_delete=models.CASCADE
    # обеспечивает связность данных:
    # если из таблицы User будет удалён пользователь,
    # то будут удалены все связанные с ним посты.
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    class Meta:
        ordering = ('pub_date',)
