# Проект Yatube

[![CI](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml)

## Описание

Yatube - это социальная сеть с авторизацией, персональными лентами, комментариями и подписками на авторов статей.

### Технологии

Python 3.9
Django 2.2.19

### Установка

1. Клонировать репозиторий:

   ```python
   git clone https://github.com/Ural207/hw03_forms.git
   ```

2. Установить виртуальное окружение для проекта:

   ```python
   python3.9 -m venv venv
   ```

3. Активировать виртуальное окружение для проекта:

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

4. Установить зависимости:

   ```python
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Выполнить миграции на уровне проекта:

   ```python
   cd yatube
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. Запустить проект локально:

   ```python
   python3 manage.py runserver

   # адрес запущенного проекта
   http://127.0.0.1:8000
   ```

### Автор
Атауллин Урал, студент Яндекс практикумa.
