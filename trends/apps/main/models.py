from django.utils import timezone
import datetime, os
from django.contrib import admin
from django.shortcuts import reverse

from django.db import models


class Proffessions(models.Model):
    name = models.CharField(verbose_name="Профессия", max_length=60)
    rating_position = models.CharField(verbose_name="Позиция в рейтинге", max_length=10)
    vacancies_count = models.CharField(verbose_name="Количество вакансий", max_length=60)
    frequencies_count = models.CharField(verbose_name="Количество запросов", max_length=60)
    change = models.CharField(verbose_name="Изменение за месяц", max_length=60)
    coeff = models.CharField(verbose_name="Коэффициент изменения", max_length=10, default = '-')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class Frequencies(models.Model):
    name = models.CharField(verbose_name="Профессия", max_length=60)
    count = models.CharField(verbose_name="Количество запросов", max_length=60)
    date = models.DateTimeField(verbose_name='Дата')
    coeff = models.CharField(verbose_name="Коэффициент изменения", max_length=10, default = '-')

    def __str__(self):
        return self.name + ' - ' + self.date.strftime('%d-%m-%Y')

    class Meta():
        verbose_name = "Частотность запросов"
        verbose_name_plural = "Частотности запросов"

class Vacancies(models.Model):
    name = models.CharField(verbose_name="Профессия", max_length=60)
    count = models.CharField(verbose_name="Количество вакансий", max_length=60)
    date = models.DateTimeField(verbose_name='Дата')
    coeff = models.CharField(verbose_name="Коэффициент изменения", max_length=10, default = '-')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Количество вакансий"
        verbose_name_plural = "Количество вакансий"

class Marks(models.Model):
    date = models.DateTimeField(verbose_name='Дата')
    text = models.TextField(verbose_name = "Текст метки")
    article = models.TextField(verbose_name = "Статья")

    def __str__(self):
        return '{0} - {1}'.format(self.date, self.id)

    class Meta():
        verbose_name = "Метка"
        verbose_name_plural = "Метки"

admin.site.register(Frequencies)
admin.site.register(Vacancies)
admin.site.register(Marks)
admin.site.register(Proffessions)