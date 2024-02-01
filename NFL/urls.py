from django.urls import path
from NFL.views import fixtures, responses

urlpatterns = [
    path('get-fixtures', fixtures.get_fixtures, name='get-fixtures'),
    path('load-fixtures', fixtures.load_fixtures_from_json, name='load-fixtures'),
    path('load-results', fixtures.load_results_from_json, name='load-results'),
    path('responses', responses.receive_response, name='responses'),
    path('tally-responses', responses.tally_responses, name='tally_responses')
]
