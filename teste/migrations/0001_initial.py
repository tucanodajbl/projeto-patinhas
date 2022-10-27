# Generated by Django 3.2.15 on 2022-10-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Código', models.IntegerField(max_length=6)),
                ('Nome', models.CharField(max_length=50)),
                ('Raça', models.CharField(max_length=50)),
                ('Porte', models.CharField(max_length=50)),
                ('Idade_Aproximada', models.IntegerField()),
                ('Cor_do_Pelo', models.CharField(max_length=50)),
                ('Observações', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='func',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuário', models.CharField(max_length=50)),
                ('Senha', models.CharField(max_length=20)),
            ],
        ),
    ]
