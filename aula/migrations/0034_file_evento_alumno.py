# Generated by Django 2.1.2 on 2019-02-04 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aula', '0033_file_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_evento',
            name='alumno',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Alumno'),
            preserve_default=False,
        ),
    ]