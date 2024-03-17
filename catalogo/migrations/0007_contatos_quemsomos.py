# Generated by Django 5.0.3 on 2024-03-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_alter_brinquedos_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.IntegerField(default=None)),
                ('gmail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='titulo', max_length=1)),
                ('texto', models.CharField(default='', max_length=250)),
            ],
        ),
    ]
