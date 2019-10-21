# Generated by Django 2.2.5 on 2019-10-21 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Personales',
            fields=[
                ('idDatosPer', models.IntegerField(primary_key=True, serialize=False)),
                ('Primer_Nombre', models.CharField(max_length=30)),
                ('Segundo_Nombre', models.CharField(max_length=30)),
                ('Primer_Apellido', models.CharField(max_length=30)),
                ('Segundo_Apellido', models.CharField(max_length=30)),
                ('Domicilio', models.CharField(max_length=30)),
                ('Comuna', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=30)),
                ('Rut', models.CharField(max_length=30)),
                ('Nacionalidad', models.CharField(max_length=30)),
                ('Fecha_Nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('datos_personales_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.Datos_Personales')),
                ('Cargo', models.IntegerField()),
                ('Email', models.CharField(max_length=30)),
            ],
            bases=('login.datos_personales',),
        ),
    ]
