# Generated by Django 2.1.2 on 2018-12-13 11:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aula', '0008_remove_asignatura_id_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_asignatura',
            name='id_asignatura',
        ),
        migrations.AddField(
            model_name='user_asignatura',
            name='id_asignatura',
            field=models.ManyToManyField(to='aula.Asignatura', verbose_name='Id asignatura'),
        ),
        migrations.RemoveField(
            model_name='user_asignatura',
            name='id_user',
        ),
        migrations.AddField(
            model_name='user_asignatura',
            name='id_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Id usuario'),
        ),
    ]
