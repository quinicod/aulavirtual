# Generated by Django 2.1.2 on 2019-02-05 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0035_auto_20190204_1736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file_evento',
            options={'ordering': ['-created'], 'verbose_name': 'File_Evento', 'verbose_name_plural': 'File_Eventos'},
        ),
        migrations.AddField(
            model_name='file_evento',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file_evento',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
    ]
