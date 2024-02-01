import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from NFL.models.fixture import Fixture

import logging

logger = logging.getLogger("django")


def get_fixtures_by_division(division: int, year: int, fixtures: dict) -> dict:
    """Get fixtures by division."""
    db_fixtures = Fixture.objects.filter(division=division, year=year)
    for fixture in db_fixtures:
        rounds = fixtures.setdefault("round", {})
        league_round = rounds.setdefault(fixture.league_round, {})
        league_round.setdefault("deadline", fixture.deadline)
        division = league_round.setdefault("division", {})
        matches = division.setdefault(fixture.division, [])
        matches.append({
            "homeTeam": fixture.home_team,
            "awayTeam": fixture.away_team
        })
    return fixtures


def load_results(results):
    for result in results:
        division = int(result["division"])
        league_round = int(result["round"])
        fixture = Fixture.objects.get(home_team=result.get("homeTeam"), away_team=result.get("awayTeam"),
                                      league_round=league_round, year=result.get("year"), division=division)
        fixture.result = result.get("result")
        fixture.save()


def load_fixtures(fixtures):
    for fixture in fixtures:
        new_fixture = Fixture()
        new_fixture.home_team = fixture["homeTeam"]
        new_fixture.away_team = fixture["awayTeam"]
        new_fixture.division = int(fixture["division"].split()[1])
        new_fixture.year = fixture["year"]
        new_fixture.league_round = int(fixture["round"].split()[1])
        if fixture.get("deadline", False):
            new_fixture.deadline = datetime.strptime(fixture["deadline"], "%Y-%m-%d %H:%M:%S")
        new_fixture.save()
