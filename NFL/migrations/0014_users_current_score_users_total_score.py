# Generated by Django 4.1 on 2023-03-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFL', '0013_results_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='current_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='total_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]