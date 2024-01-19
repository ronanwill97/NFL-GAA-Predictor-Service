# Generated by Django 4.1 on 2024-01-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFL', '0019_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='round',
            new_name='league_round',
        ),
        migrations.AddField(
            model_name='fixture',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='result',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
