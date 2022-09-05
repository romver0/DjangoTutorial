from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from myapp.models import Car

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
menu = {
    'about': "О сайте",
    'addPost': "Добавить статью",
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
        }
    }
    return render(request, 'filter.html', context=context)


def index(request):
    # return HttpResponse('Домашнаяя страница')
    # return HttpResponse('''
    # <html>
    # <head>
    #          <title>Заголовок</title>
    # </head>
    # <body>
    #     Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    # </body>
    # </html>
    # ''')
    # car = Car.objects.all()
    car = Car.objects.order_by('-time_update')
    context = {
        'cars': car,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'about.html', context=context)


def addPost(request):
    context = {
        'menu': menu,
        'title': 'Добавить статью'
    }
    return render(request, 'addPost.html', context=context)


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


'''
    handler500 - ошибка сервера
    handler403 - доступ запрещён
    handler400 - невозможно обработать запрос
'''
