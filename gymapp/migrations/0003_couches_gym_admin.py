# Generated by Django 4.0.3 on 2022-04-18 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymapp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='couches',
            name='gym_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ст. тренер'),
        ),
    ]
