import os

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from NFL.utils.fixtures import *
from datetime import datetime
import json
import logging

logger = logging.getLogger("django")


@csrf_exempt
def get_fixtures(request):
    league_round = os.environ.get('LEAGUE_ROUND', False)
    year = int(request.GET.get('year', datetime.now().year))
    fixtures = {}
    for division in [1, 2, 3, 4]:
        fixtures = get_fixtures_by_division(division, year, fixtures)
    if league_round:
        league_rounds = fixtures.get("round", {})
        fixtures_for_round = {int(league_round): league_rounds.get(int(league_round), {})}
        return (JsonResponse(fixtures_for_round))

    return (JsonResponse(fixtures))


@csrf_exempt
def load_results_from_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            load_results(data)
        except (json.JSONDecodeError, KeyError):
            return HttpResponseBadRequest('Invalid request data')
        except Exception as e:
            return HttpResponseServerError(e)

        return HttpResponse("SUCCESS")
    else:
        return HttpResponseBadRequest('Invalid request method')


@csrf_exempt
def load_fixtures_from_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            load_fixtures(data)
        except (json.JSONDecodeError, KeyError):
            return HttpResponseBadRequest('Invalid request data')
        except Exception as e:
            return HttpResponseServerError(e)

        return HttpResponse("SUCCESS")
    else:
        return HttpResponseBadRequest('Invalid request method')
