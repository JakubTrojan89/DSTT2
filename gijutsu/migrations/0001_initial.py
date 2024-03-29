# Generated by Django 5.0.1 on 2024-01-30 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MartialArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='TechniqueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=512)),
                ('martial_arts', models.ManyToManyField(to='gijutsu.martialart')),
                ('technique_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gijutsu.techniquetype')),
            ],
        ),
        migrations.CreateModel(
            name='BeltRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=512)),
                ('martial_arts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gijutsu.martialart')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gijutsu.technique')),
            ],
        ),
    ]
