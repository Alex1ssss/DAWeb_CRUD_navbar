# Generated by Django 5.1 on 2024-11-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_cliente', models.CharField(max_length=6)),
                ('fecha', models.DateField()),
                ('total_venta', models.PositiveIntegerField()),
                ('metodo_pago', models.CharField(max_length=20)),
                ('id_empleado', models.CharField(max_length=6)),
            ],
        ),
    ]
