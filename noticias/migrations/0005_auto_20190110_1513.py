# Generated by Django 2.1.2 on 2019-01-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20190110_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias', verbose_name='Imagen'),
        ),
    ]
