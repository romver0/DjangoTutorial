from django.db import models


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
        return self.title+'🚗'

    def func(self):
        print('вызов func')