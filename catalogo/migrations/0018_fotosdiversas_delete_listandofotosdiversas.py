# Generated by Django 5.0.3 on 2024-03-17 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0017_listandofotosdiversas_alter_brinquedos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosDiversas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime.now)),
                ('publicada', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ListandoFotosDiversas',
        ),
    ]