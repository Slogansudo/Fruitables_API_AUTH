# Generated by Django 5.0.4 on 2024-05-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_album_options_alter_artist_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='famous_rating',
            field=models.BooleanField(default=False),
        ),
    ]
