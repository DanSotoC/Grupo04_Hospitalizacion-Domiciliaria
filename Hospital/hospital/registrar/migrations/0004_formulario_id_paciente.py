# Generated by Django 3.0.3 on 2020-03-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0003_auto_20200307_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='id_paciente',
            field=models.IntegerField(default=0),
        ),
    ]