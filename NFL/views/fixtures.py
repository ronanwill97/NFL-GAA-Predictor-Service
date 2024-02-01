# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from NFL.utils.fixtures import *
from datetime import datetime
import os


@api_view(['GET'])
def get_fixtures(request):
    league_round = os.environ.get('LEAGUE_ROUND', False)
    year = int(request.query_params.get('year', datetime.now().year))
    fixtures = {}
    for division in [1, 2, 3, 4]:
        fixtures = get_fixtures_by_division(division, year, fixtures)
    if league_round:
        league_rounds = fixtures.get("round", {})
        fixtures_for_round = {int(league_round): league_rounds.get(int(league_round), {})}
        return Response(fixtures_for_round)

    return Response(fixtures)


@api_view(['POST'])
def load_results_from_json(request):
    try:
        data = request.data  # DRF handles JSON parsing
        load_results(data)
    except KeyError:
        return Response('Invalid request data', status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response("SUCCESS")


@api_view(['POST'])
def load_fixtures_from_json(request):
    try:
        data = request.data  # DRF handles JSON parsing
        load_fixtures(data)
    except KeyError:
        return Response('Invalid request data', status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response("SUCCESS")
