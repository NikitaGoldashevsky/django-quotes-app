# Django Quotes App

Django-приложение для отображения случайных цитат и рейтинга лучших цитат.  
Доступно онлайн: [NikGld.pythonanywhere.com](https://NikGld.pythonanywhere.com/)

---

## Функционал

- Случайная цитата — главная страница показывает случайную цитату из базы.  
- Топ цитат — рейтинг цитат по количеству лайков.  
- Админ-панель Django — возможность управлять цитатами через `/admin/`.  
- Простой UI — аккуратная навигация и стилизованный интерфейс.  

---

## Технологии

- Python 3.10+
- Django 5
- SQLite (по умолчанию, можно сменить на PostgreSQL/MySQL)
- CSS (чистый, без фреймворков)

---

## Запуск локально

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/<username>/django-quotes-app.git
   cd django-quotes-app/quotesapp
   ```

2. Создать виртуальное окружение и активировать:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Применить миграции и собрать статику:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

5. Запустить сервер:
   ```bash
   python manage.py runserver
   ```

6. Открыть в браузере:
   ```
   http://127.0.0.1:8000/
   ```

---

## Доступ в админку

1. Создать суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
2. Войти в админку:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## Деплой

Приложение развернуто на [PythonAnywhere](https://www.pythonanywhere.com/).  
Для деплоя использовались:
- virtualenv с зависимостями из `requirements.txt`
- настройка `WSGI` и `ALLOWED_HOSTS`
- `collectstatic` для статики  

---

## Лицензия

MIT License © 2025 [LICENSE](LICENSE).
