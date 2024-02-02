# Generated by Django 5.0.1 on 2024-02-02 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gijutsu', '0003_beltranking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beltranking',
            old_name='martial_arts',
            new_name='martial_art',
        ),
        migrations.RenameField(
            model_name='technique',
            old_name='martial_arts',
            new_name='martial_art',
        ),
        migrations.CreateModel(
            name='MartialArtLegends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('martial_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gijutsu.martialart')),
            ],
        ),
    ]