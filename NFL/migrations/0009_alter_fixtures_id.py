# Generated by Django 4.1 on 2023-03-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFL', '0008_remove_fixtures_away_team_remove_fixtures_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
