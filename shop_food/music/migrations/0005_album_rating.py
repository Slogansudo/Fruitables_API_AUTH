# Generated by Django 5.0.4 on 2024-05-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_songs_music_songs_id_8977f4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]