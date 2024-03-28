import math
from django.core.paginator import Paginator, Page
from django.http import HttpRequest
from recipes.models import Recipe


def make_pagination_range(page_range: list[int], qty_pages: int, current_page: int) -> dict:
    middle_range: int = math.ceil(qty_pages / 2)
    start_range: int = current_page - middle_range
    stop_range: int = current_page + middle_range
    total_pages: int = len(page_range)

    start_range_offset: int = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if start_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
    }


def make_pagination(request: HttpRequest, recipes: Recipe, per_page: int, qty_pages: int) -> dict:
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator: Paginator = Paginator(recipes, per_page)
    page_object: Page = paginator.get_page(current_page)

    pagination_range = make_pagination_range(paginator.page_range, qty_pages, current_page)

    return {
        'page_object': page_object,
        'pagination_range': pagination_range,
    }
