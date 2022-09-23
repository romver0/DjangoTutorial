from django.db import models
from django.urls import reverse


class Car(models.Model):
    PRICE_CHOICES = [
        ('N', 'Не продаётся'),
        ('M', 'По корману'),
        ('MM', 'Придётся взять в кредит'),
        ('MMM', 'Не вариант')
    ]

    title = models.CharField(max_length=255, verbose_name='Название тачки')
    price = models.CharField(
        max_length=3,
        choices=PRICE_CHOICES, default='N',
        verbose_name='Цена'
    )
    content = models.TextField(verbose_name='Описание+характеристики')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              verbose_name='фото авто',
                              # default='photos/test/font1.png',
                              )  # В параметр upload_to можно прописывать шаблон.Например, %Y/%m/%d описывает вложенные папки как год,месяц,день
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    # магический метод
    def __str__(self):
        return self.title + '🚗'

    def func(self):
        print('вызов func')

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'post_id': self.pk
        })

    def get(self):
        return self.title

    '''
    Почему это лучше тега url? Представьте, 
    что в будущем мы изменили шаблон этой ссылки и стали
     выводить посты не по id, а по слагу. Тогда, 
     при использовании тега url, нам пришлось бы менять эти ссылки
      в каждом шаблоне, заменяя self.pk на self.slug, например. 
      В этом как раз неудобство и источник потенциальных ошибок. 
      Теперь, с методом get_absolute_url() 
      нам достаточно изменить маршрут в нем и это автоматически скажется на всех шаблонах, где она используется.
    '''


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={
            'category_id': self.pk
        })

    '''
    про db_index
    Это не совсем специфично для джанго; больше связано с базами данных. Вы добавляете индексы в столбцы, когда хотите ускорить поиск в этом столбце.    
    Обычно база данных индексирует только первичный ключ. Это означает, что поиск с использованием первичного ключа оптимизирован.
    Если вы выполняете много операций поиска во вторичном столбце, рассмотрите возможность добавления индекса к этому столбцу, чтобы ускорить процесс.
    Имейте в виду, что, как и большинство проблем с масштабом, они применимы только в том случае, если у вас есть статистически большое количество строк (10 000 — это немного).
    Кроме того, каждый раз, когда вы выполняете вставку, необходимо обновлять индексы. Поэтому будьте осторожны, в какой столбец вы добавляете индексы.
    Как всегда, вы можете оптимизировать только то, что можете измерить, поэтому используйте EXPLAINоператор и журналы вашей базы данных (особенно любые журналы медленных запросов), чтобы узнать, где могут быть полезны индексы.
    '''

#
# class ExamplePerson(models.Model):
#     CHOICES = (
#         ('M', 'мужик'),
#         ('F', 'девушка')
#     )
#     name = models.CharField()
#     sex = models.CharField(max_length=1, choices=CHOICES)
#     age = models.IntegerField()
#
#     def get_absolute_url(self):
#         return reverse('myurl', kwargs={
#             'id': self.id,
#             'name': self.name
#         })
#
#     def get_absolute_url2(self):
#         return f'/person/{self.name}/'

