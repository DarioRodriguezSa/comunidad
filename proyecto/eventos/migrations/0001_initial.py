# Generated by Django 4.2.6 on 2023-10-30 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'estate',
                'verbose_name_plural': 'estates',
                'db_table': 'estate',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'tipo',
                'verbose_name_plural': 'tipos',
                'db_table': 'tipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.DateField(max_length=100, verbose_name='Titulo')),
                ('invitante', models.CharField(max_length=100, verbose_name='Invitante')),
                ('fecha', models.DateField(max_length=25)),
                ('encargado', models.CharField(max_length=75, verbose_name='Encargado')),
                ('staff', models.CharField(max_length=100, verbose_name='Staff')),
                ('lugar', models.CharField(max_length=100, verbose_name='Lugar')),
                ('noasistentes', models.IntegerField(max_length=5, verbose_name='Noasistentes')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.estate')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.tipo')),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
                'db_table': 'evento',
                'ordering': ['-id'],
            },
        ),
    ]
