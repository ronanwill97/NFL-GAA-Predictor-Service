# Generated by Django 4.1 on 2024-01-18 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFL', '0017_alter_results_away_goals_alter_results_away_points_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entries',
        ),
        migrations.RemoveField(
            model_name='results',
            name='fixture',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='Fixtures',
        ),
        migrations.DeleteModel(
            name='Results',
        ),
    ]
