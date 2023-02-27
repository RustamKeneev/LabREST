from django.db import models
from analyze.models import Analyze, Category


class Laboratory(models.Model):
    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='laboratory/images')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    address = models.CharField(max_length=200, verbose_name='Адрес аптеки')
    website = models.URLField(null=True, blank=True, verbose_name='Веб сайт (url)')
    date = models.DateTimeField(auto_now_add=True, null=True)
    analyze_laboratory = models.ManyToManyField(Analyze)

    def __str__(self):
        return self.title


