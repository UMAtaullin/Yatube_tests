from django.conf import settings
from django.core.paginator import Paginator


def paginator(posts, request):
    paginator = Paginator(posts, settings.LIMIT_POSTS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
