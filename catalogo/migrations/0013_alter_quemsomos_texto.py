# Generated by Django 5.0.3 on 2024-03-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_alter_quemsomos_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quemsomos',
            name='texto',
            field=models.TextField(default='', max_length=1000),
        ),
    ]