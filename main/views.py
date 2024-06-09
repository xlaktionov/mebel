from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о самом магазине (шаблон)'
    }
    return render(request, 'main/about.html', context)
