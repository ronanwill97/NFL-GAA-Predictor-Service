# Generated by Django 4.1 on 2023-03-01 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFL', '0002_rename_awayteam_entries_away_team_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='entries',
            table='nfl.entries',
        ),
        migrations.AlterModelTable(
            name='users',
            table='nfl.users',
        ),
    ]