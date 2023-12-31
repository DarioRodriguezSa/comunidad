# Generated by Django 4.2.6 on 2023-11-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='alquiler',
            field=models.TextField(verbose_name='Alquiler'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='combustible',
            field=models.TextField(verbose_name='Combustible'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='donaciones',
            field=models.TextField(verbose_name='Donaciones'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='otros',
            field=models.TextField(verbose_name='Otros'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='personal',
            field=models.TextField(verbose_name='Personal'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='presupuesto',
            field=models.TextField(verbose_name='Presupuesto'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='residuo',
            field=models.TextField(verbose_name='Residuo'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='totalgastado',
            field=models.TextField(verbose_name='Totalgastado'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='transporte',
            field=models.TextField(verbose_name='Trasporte'),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='viaticos',
            field=models.TextField(verbose_name='Viaticos'),
        ),
    ]
