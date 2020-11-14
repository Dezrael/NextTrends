# Generated by Django 3.1.3 on 2020-11-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201114_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proffessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Профессия')),
                ('rating_position', models.CharField(max_length=10, verbose_name='Позиция в рейтинге')),
                ('vacancies_count', models.CharField(max_length=60, verbose_name='Количество вакансий')),
                ('frequencies_count', models.CharField(max_length=60, verbose_name='Количество запросов')),
                ('change', models.CharField(max_length=60, verbose_name='Изменение за месяц')),
                ('coeff', models.CharField(default='-', max_length=10, verbose_name='Коэффициент изменения')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
    ]
