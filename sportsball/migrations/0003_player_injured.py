# Generated by Django 4.0.2 on 2022-02-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsball', '0002_remove_player_injured'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='injured',
            field=models.BooleanField(default=False),
        ),
    ]
