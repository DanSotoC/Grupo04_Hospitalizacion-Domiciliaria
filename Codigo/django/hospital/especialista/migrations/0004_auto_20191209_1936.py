# Generated by Django 2.2.5 on 2019-12-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialista', '0003_paciente_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]