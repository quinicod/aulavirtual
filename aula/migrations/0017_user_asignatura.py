# Generated by Django 2.1.2 on 2018-12-13 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aula', '0016_auto_20181213_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('id_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.Asignatura', verbose_name='Id asignatura')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id usuario')),
            ],
            options={
                'verbose_name': 'User_asignatura',
                'verbose_name_plural': 'User_asignaturas',
                'ordering': ['-created'],
            },
        ),
    ]
