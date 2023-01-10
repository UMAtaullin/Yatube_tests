from django.shortcuts import render


def page_not_found(request, exception):
    """Переопределение страницы с ошибкой 404."""
    return render(request, 'core/404.html', {'path': request.path}, status=404)
