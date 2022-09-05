from django.db import models
from django.urls import reverse


class Car(models.Model):
    PRICE_CHOICES = [
        ('M', 'По корману'),
        ('MM', 'Придётся взять в кредит'),
        ('MMM', 'Не вариант')
    ]

    title = models.CharField(max_length=255, verbose_name='Название тачки')
    price = models.CharField(
        max_length=3,
        choices=PRICE_CHOICES, default='норм',
        verbose_name='Цена'
    )
    content = models.TextField(verbose_name='Описание+характеристики')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",
                              verbose_name='фото авто')  # В параметр upload_to можно прописывать шаблон.Например, %Y/%m/%d описывает вложенные папки как год,месяц,день
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title + '🚗'

    def func(self):
        print('вызов func')

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'post_id': self.pk
        })
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
