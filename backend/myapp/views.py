from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from myapp.models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu = {
    'about': "О сайте",
    'addpage': "Добавить статью",
    'feedback': "Обратная связь",
    'login': "Войти",
}


def filterViews(request):
    len = [1, 2, 3]
    text = "<b>Lorem</b> ipsum <bdi>dolor</bdi>"
    test = Car.objects.all()
    context = {
        'test': test,
        'car': test[0].title,
        'text': text,
        'len': len,
        'dict_': {
            'value1': 'a',
            'value2': 'b',
            'value3': 'c',
        },
        'static_len': 0,
    }
    return render(request, 'filter.html', context=context)


def index(request):
    car = Car.objects.order_by('-time_update')
    category = Category.objects.order_by('name')
    context = {
        'cars': car,
        'categories': category,
        'menu': menu,
        'len': car.count(),
        'title': 'Главная страница',
        'categories_selected': 0
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'about.html', context=context)


def addpage(request):
    return render(request, 'addpage.html')


def post(request, post_id):
    context = {
        'post_id': post_id,
    }
    print(request.GET)
    return render(request, 'post.html', context=context)


def feedback(request):
    return render(request, 'feedback.html')


def login(request):
    return render(request, 'login.html')


# def categories(request, car_id):
#     return HttpResponse(f"<h1>Статья по категориям</h1> {car_id}")
def categories(request, type):
    if type == 'return':
        print('сработал ')
        return redirect('home', permanent=True)  # redirect 301(постоянный адрес)
    return HttpResponse(f"<h1>Статья по категориям</h1> {type}")


def archive(request, year):
    if int(year) > 2022:
        # raise Http404()
        return HttpResponseNotFound('<h1>Превышен лимит</h1>')
    '''    http://127.0.0.1:8000/archive/2002/?name=Roman&age=20&city=%D0%9D%D0%BE%D0%B2%D0%BE%D1%87%D0%B5%D0%B1%D0%BE%D0%BA%D1%81%D0%B0%D1%80%D1%81%D0%BA
        <QueryDict: {'name': ['Roman'], 'age': ['20'], 'city': ['Новочебоксарск']}>
    '''
    if request.GET:
        print(request.GET)
        print(request.GET.get('name'))
        return HttpResponse(f"<h1>Архив по годам {year}</h1>\n"
                            f"{request.GET}")
    else:
        return HttpResponse(f"<h1>Архив по годам {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена,Сэр</h1>')


def show_category(request, category_id):
    car = Car.objects.order_by('-time_update')
    category = Category.objects.order_by('name')
    context = {
        'cars': car,
        'categories': category,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'categories_selected': category_id
    }
    return render(request, 'index.html', context=context)


'''
    handler500 - ошибка сервера
    handler403 - доступ запрещён
    handler400 - невозможно обработать запрос
'''
