# Generated by Django 2.1.2 on 2019-01-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0026_auto_20190116_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
