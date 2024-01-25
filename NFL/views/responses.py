from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from NFL.utils.responses import *
import logging
import json

logger = logging.getLogger("django")


@csrf_exempt
def receive_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if isinstance(data, list):
                for response in data:
                    save_response(response)
            else:
                logger.info(data)
                save_response(data)
        except (json.JSONDecodeError, KeyError):
            return HttpResponseBadRequest('Invalid request data')
        except Exception as e:
            return HttpResponseServerError(e)

        return HttpResponse("SUCCESS")
    else:
        return HttpResponseBadRequest('Invalid request method')


@csrf_exempt
def tally_responses(request):
    league_round = request.GET.get('round', 1)
    year = int(request.GET.get('year', datetime.now().year))
    scores = calculate_scores(league_round, year)

    sorted_scores = sort_scores(scores)
    return (JsonResponse(sorted_scores, safe=False))
