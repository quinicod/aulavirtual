# Generated by Django 2.1.2 on 2018-12-13 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0004_auto_20181213_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario_curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('id_calendario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aula.Calendario', verbose_name='Id Calendario')),
                ('id_curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aula.Curso', verbose_name='Id Curso')),
            ],
            options={
                'verbose_name': 'Calendario_curso',
                'verbose_name_plural': 'Calendario_cursos',
                'ordering': ['-created'],
            },
        ),
    ]