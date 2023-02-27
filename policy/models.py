from django.db import models


class Policy(models.Model):
    class Meta:
        verbose_name = 'Конфицидиальность'
        verbose_name_plural = 'Конфицидиальность'
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title