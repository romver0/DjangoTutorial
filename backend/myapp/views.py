from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Домашнаяя страница')


# def categories(request, car_id):
#     return HttpResponse(f"<h1>Статья по категориям</h1> {car_id}")

def categories(request, type):
    if type == 'return':
        print('сработал ')
        return redirect('home', permanent=True) # redirect 301(постоянный адрес)
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
