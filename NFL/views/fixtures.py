from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from NFL.utils.get_football_fixtures import *
from NFL.utils.get_football_results import *
from datetime import datetime


def getFixtures(request):
    league_round = request.GET.get('round', None)
    fixtures = {}
    for division in [1, 2, 3, 4]:
        fixtures = get_fixtures_by_division(division, fixtures)

    if league_round is not None:
        return (JsonResponse(fixtures[f"Round {league_round}"]))

    return (JsonResponse(fixtures))


def getResults(request):
    results = {}
    league_round = request.GET.get('round', 1)
    year = int(request.GET.get('year', datetime.year))
    for division in [1, 2, 3, 4]:
        results = get_results_by_division(division, year, results)

    if league_round is not None:
        return (JsonResponse(results[league_round]))

    return (JsonResponse(results))

# @csrf_exempt)
# def submitEntry(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             selections = data['data']
#             details = data['details']
#             email = details['email']
#             name = details['fullName']
#             number = details['phone']
#             address = details['address']
#             user,userCreated = Users.objects.get_or_create(email=email,name=name,number=number,address=address)
#             user.save()
#             for fixture in selections:
#                 homeTeam = fixture['homeTeam']
#                 awayTeam = fixture['awayTeam']
#                 option = fixture['selectedOption']
#                 email = details['email']
#                 entry,created = Entries.objects.get_or_create(
#                     email=email,
#                     home_team=homeTeam,
#                     away_team=awayTeam,
#                     selected_option=option,
#                     user_id=user.id)
#                 entry.save()
#                 # Do something with the data (e.g. save to database)
#             return JsonResponse({'status': 'success'})
#         except (json.JSONDecodeError, KeyError):
#             return HttpResponseBadRequest('Invalid request data')
#     else:
#         return HttpResponseBadRequest('Invalid request method')
#
#
#
#
#
