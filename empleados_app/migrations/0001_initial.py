# Generated by Django 5.1.3 on 2024-11-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.PositiveBigIntegerField()),
                ('correo', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('puesto', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
