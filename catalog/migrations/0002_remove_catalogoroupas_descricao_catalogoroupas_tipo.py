# Generated by Django 5.0.6 on 2024-06-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogoroupas',
            name='descricao',
        ),
        migrations.AddField(
            model_name='catalogoroupas',
            name='tipo',
            field=models.CharField(choices=[('camiseta', 'Camiseta'), ('calca', 'Calça'), ('bermuda', 'Bermuda'), ('tenis', 'Tenis'), ('casaco', 'Casaco')], default='camiseta', max_length=20),
        ),
    ]
