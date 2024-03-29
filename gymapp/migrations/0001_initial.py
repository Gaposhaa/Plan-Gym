# Generated by Django 4.0.3 on 2022-04-10 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('coach_information', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='SportStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('direction_information', models.TextField(verbose_name='Описание направления')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_training', models.CharField(max_length=15, verbose_name='Количество тренировок')),
                ('price', models.CharField(max_length=5, verbose_name='Цена(бел/руб)')),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymapp.couches')),
                ('sport_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymapp.sportstyle')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Прайс-лист',
            },
        ),
    ]
