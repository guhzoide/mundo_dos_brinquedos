# Generated by Django 5.0.3 on 2024-03-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_contatos_categoria_contatos_publicada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brinquedos',
            name='descricao',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='texto',
            field=models.TextField(default='', max_length=250),
        ),
    ]
