# Generated by Django 2.1.2 on 2018-12-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0007_auto_20181213_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='id_nivel',
        ),
    ]