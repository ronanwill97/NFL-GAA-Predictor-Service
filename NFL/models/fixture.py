from django.db import models


class Fixture(models.Model):
    home_team = models.CharField(max_length=255, null=False)
    away_team = models.CharField(max_length=255, null=False)
    result = models.CharField(max_length=255, null=True)
    division = models.IntegerField(null=False)
    year = models.IntegerField(null=False)
    league_round = models.IntegerField(null=False)
    deadline = models.DateTimeField(null=True)

    class Meta:
        app_label = 'NFL'
        unique_together = ['home_team', 'away_team', 'year', 'league_round']
