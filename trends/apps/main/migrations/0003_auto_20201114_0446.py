# Generated by Django 3.1.3 on 2020-11-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201114_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencies',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Профессия'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Профессия'),
        ),
    ]
