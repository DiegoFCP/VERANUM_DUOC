# Generated by Django 5.0.6 on 2024-07-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id_habitacion', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('caracteristicas', models.CharField(max_length=500)),
                ('precio', models.IntegerField()),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hoteles',
            fields=[
                ('id_hotel', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiciosExtras',
            fields=[
                ('id_serv_extras', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
    ]
