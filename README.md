# 1. Описание системы

### Система состоит из следующих функциональных блоков:
## MVP
- регистрация, авторизация и аутентефикация
- разделение прав для админа и обычного пользователя 
- функционал для админа: управление каталогом продуктов, добавление/изменение/удаление категорий десертов (торты, пирожные и т.д.)
- функционал для обычного пользователя: личный кабинет, корзина заказов
- форма обратной связи
- фильты для поиска
- поиск по сайту
- Информ страница о доставке и оплате

## Extantions
- ссылки на соцсети
- Отображение 3-х последних постов инстаграм
- API google maps
- Сохранение статики на AWS S3
- Деплой на сервер AWS EC2
- Использование Celery/Redis для асинхронных задач


# 2. Типы пользователей
Администратор: 
- создание категорий десертов
- добавление десертов в соответствующую категорию
- просмотр всех заказов пользователей

Простой пользаватель:
- возможность регистрации и авторизации, добавить десерт в корзину, сделать заказ