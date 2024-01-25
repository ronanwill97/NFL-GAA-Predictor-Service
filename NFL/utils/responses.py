from datetime import datetime
from NFL.models.response import Response
from NFL.models.fixture import Fixture
import uuid

import logging

logger = logging.getLogger("django")


def score_prediction(prediction, fixture) -> int:
    home_team = fixture.home_team
    away_team = fixture.away_team
    actual_winner = fixture.result
    if prediction == actual_winner:
        if actual_winner == "Draw":
            return 8
        if actual_winner == home_team:
            return 4
        if actual_winner == away_team:
            return 5
    return 0


def calculate_scores(league_round: int, year: int):
    scores = {}
    fixtures = Fixture.objects.filter(league_round=league_round, year=year)
    for fixture in fixtures:
        responses = Response.objects.filter(fixture=fixture)
        for response in responses:
            form_uuid = str(response.form_uuid)
            if scores.get(form_uuid, False):
                scores[form_uuid]["points"] += score_prediction(response.selection, fixture)
            else:
                form = scores.setdefault(form_uuid, {})
                form["points"] = score_prediction(response.selection, fixture)
                form["name"] = response.name
                form["phoneNumber"] = response.phone_number

    return scores


def sort_scores(scores):
    sorted_scores = {}
    for form_uuid, score in scores.items():
        phoneNumber = score["phoneNumber"]
        if sorted_scores.get(phoneNumber, False):
            if sorted_scores[phoneNumber]["points"] < score["points"]:
                sorted_scores[phoneNumber]["points"] = score["points"]
        else:
            new_score = sorted_scores.setdefault(phoneNumber, {})
            new_score["points"] = score["points"]
            new_score["name"] = score["name"]

    return sorted([value for key, value in sorted_scores.items()], key=lambda x: x["points"], reverse=True)


def save_response(response: dict):
    year = response.get('year', datetime.now().year)
    league_round = response.get('round', None)
    phone_number = response.get('phoneNumber', None)
    name = response.get('name', None)
    form_uuid = uuid.uuid4()
    for key, value in response.get('responses', {}).items():
        new_response = Response()
        new_response.phone_number = phone_number
        new_response.name = name
        new_response.form_uuid = form_uuid
        new_response.selection = value
        home_team, away_team = key.split("_")
        try:
            fixture = Fixture.objects.get(home_team=home_team, away_team=away_team, year=year,
                                          league_round=league_round)
            new_response.fixture = fixture
            new_response.save()
        except Fixture.DoesNotExist:
            # Handle the case where the item does not exist
            raise Exception(f"No Fixture found for {key}")
        except Fixture.MultipleObjectsReturned:
            raise Exception(f"Duplicate records found for fixture {key}")
