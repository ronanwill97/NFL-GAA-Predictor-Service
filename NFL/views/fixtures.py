from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from NFL.utils.fixtures import *
from datetime import datetime
import json
import logging

logger = logging.getLogger("django")


def get_fixtures(request):
    league_round = request.GET.get('round', False)
    year = int(request.GET.get('year', datetime.now().year))
    fixtures = {}
    for division in [1, 2, 3, 4]:
        fixtures = get_fixtures_by_division(division, year, fixtures)
    if league_round:
        round_info = fixtures.get("round", {})
        return (JsonResponse(round_info.get(int(league_round), {})))

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
