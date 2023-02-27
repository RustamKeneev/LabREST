from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    title = models.CharField(max_length=200, verbose_name='Название')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Analyze(models.Model):
    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'

    title = models.CharField('Название',max_length=256)
    description = models.TextField('Описание')
    preparationForAnalysis = models.TextField('Подготовка к анализу')
    requirements = models.TextField('Требования')
    interpretationOfResults = models.TextField('Интерпретация результатов')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    laboratoryTest = models.CharField('Лабораторные тесты', max_length=500)
    biomaterial = models.TextField('Биоматериал')
    deadlineDateOfIssueOfResults = models.CharField('срок выполнения день, выдачи результатов', max_length=300)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # price = models.IntegerField(verbose_name="Цена",null=True)

    def __str__(self):
        return f'анализы-{self.title}'


class PriceAnalyzeToLaboratory(models.Model):
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
    analyze = models.ForeignKey(Analyze, on_delete=models.CASCADE,related_name="prices")
    laboratory = models.ForeignKey('laboratory.Laboratory', on_delete=models.CASCADE, related_name="prices_lab")
    price = models.IntegerField()

    def __str__(self):
        return f'{self.price}'