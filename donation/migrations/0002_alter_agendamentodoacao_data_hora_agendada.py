# Generated by Django 5.0.6 on 2024-07-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentodoacao',
            name='data_hora_agendada',
            field=models.CharField(max_length=20),
        ),
    ]
