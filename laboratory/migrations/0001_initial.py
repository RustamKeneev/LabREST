# Generated by Django 4.0.3 on 2022-03-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analyze', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='laboratory/')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон номер')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес аптеки')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Веб сайт (url)')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('analyzes', models.ManyToManyField(blank=True, to='analyze.analyze')),
            ],
            options={
                'verbose_name': 'Лаборатория',
                'verbose_name_plural': 'Лаборатории',
            },
        ),
    ]
