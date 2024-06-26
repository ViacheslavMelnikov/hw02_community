# Приложение Post, для публикации записей и разделения их по сообществам пользователей, в дальнейших проектах планируется его доработка.
## Установка:
Клонируйте репозиторий и перейдите в него в командной строке: 
git clone git@github.com:ViacheslavMelnikov/hw02_community.git
pip install -r requirements.txt

## Описание проекта
Создание и регистрация приложения Posts.

Подключена база данных.

Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие. Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

Модели (models.py):

Post - запись. Поля:
text(текст записи) - тип поля - Текст
pub_date(дата публикации) - тип поля - Дата (автоматически добавляется текущая дата)
author(Автор) - тип поля - Ссылка на модель User (связь «один-ко-многим»)
group(Сообщество) - тип поля - Ссылка на модель Group (связь «один-ко-многим»)
Group - сообщество. Поля:
title(Имя) - тип поля - Строка
slug(Адрес) - тип поля - slug
description(Описание) - тип поля - Текст метод str возвращает имя сообщества (title)
Админка (admin.py)

Зарегистрированы модели Post, Group.

Для модели Post создана кастомная админка:

В списке объектов в админке отображаются поля pk, text, pub_date, author, group.
Содержимое поля group можно редактировать в админке прямо в списке объектов Post.
Доступен поиск по полю text.
Доступна фильтрация по полю pub_date.
Если какое-то поле не заполнено, в нём отображается текст -пусто-.
View-функции (views.py):

index(): передаёт в шаблон posts/index.html десять последних объектов модели Post.
group_posts(): передаёт в шаблон posts/group_list.html десять последних объектов модели Post, отфильтрованных по полю group, и содержимое для тега <title>.
Адреса (urls.py)

Для приложения Posts установлен namespace='posts'.
Для главной страницы установлен name='index'.
Страница с постами из определённой группы доступна по URL вида group//.
Для страницы с постами группы установлен name='group_list'.
Шаблоны:

Файлы шаблонов хранятся на уровне проекта.
Шаблоны разбиты на логические блоки и собираются с помощью тегов include и extend.
К шаблонам подключена статика.
В шаблоне index.html ссылка все записи группы адресует пользователя на страницу той группы, которой принадлежит пост.
Из view-функций в словаре context передаётся основное содержимое страницы.
Содержимое тега <title>:
для страницы группы: Записи сообщества <имя_группы>;
для главной страницы: Последние обновления на сайте.Приложение Post, для публикации записей и разделения их по сообществам пользователей, в дальнейших проектах планируется его доработка.
Установка:
после клонирования, находясь в склонированном каталоге прописать в консоли: pip install -r requirements.txt

Описание проекта
Создано и зарегистрировано приложение Posts.

Подключена база данных.

Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие. Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

Модели (models.py):

Post - запись. Поля:
text(текст записи) - тип поля - Текст
pub_date(дата публикации) - тип поля - Дата (автоматически добавляется текущая дата)
author(Автор) - тип поля - Ссылка на модель User (связь «один-ко-многим»)
group(Сообщество) - тип поля - Ссылка на модель Group (связь «один-ко-многим»)
Group - сообщество. Поля:
title(Имя) - тип поля - Строка
slug(Адрес) - тип поля - slug
description(Описание) - тип поля - Текст метод str возвращает имя сообщества (title)
Админка (admin.py)

Зарегистрированы модели Post, Group.

Для модели Post создана кастомная админка:

В списке объектов в админке отображаются поля pk, text, pub_date, author, group.
Содержимое поля group можно редактировать в админке прямо в списке объектов Post.
Доступен поиск по полю text.
Доступна фильтрация по полю pub_date.
Если какое-то поле не заполнено, в нём отображается текст -пусто-.
View-функции (views.py):

index(): передаёт в шаблон posts/index.html десять последних объектов модели Post.
group_posts(): передаёт в шаблон posts/group_list.html десять последних объектов модели Post, отфильтрованных по полю group, и содержимое для тега <title>.
Адреса (urls.py)

Для приложения Posts установлен namespace='posts'.
Для главной страницы установлен name='index'.
Страница с постами из определённой группы доступна по URL вида group//.
Для страницы с постами группы установлен name='group_list'.
Шаблоны:

Файлы шаблонов хранятся на уровне проекта.
Шаблоны разбиты на логические блоки и собираются с помощью тегов include и extend.
К шаблонам подключена статика.
В шаблоне index.html ссылка все записи группы адресует пользователя на страницу той группы, которой принадлежит пост.
Из view-функций в словаре context передаётся основное содержимое страницы.
Содержимое тега <title>:
для страницы группы: Записи сообщества <имя_группы>;
для главной страницы: Последние обновления на сайте.

## Автор
Вячеслав Мельников
https://t.me/Rqprograz
