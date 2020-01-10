# Generated by Django 3.0.1 on 2020-01-09 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=50)),
                ('num_domicilio', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('f_nacimiento', models.CharField(max_length=20)),
                ('id_perfil', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido1', models.CharField(max_length=30)),
                ('apellido2', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=50)),
                ('num_domicilio', models.CharField(max_length=50)),
                ('edad_paciente', models.IntegerField(null=True)),
                ('f_nacimiento', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
                ('rut_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Tutor')),
            ],
        ),
    ]
