from django.urls import path
from NFL.views import fixtures, responses

urlpatterns = [
    path('api/get-fixtures', fixtures.get_fixtures, name='get-fixtures'),
    path('api/load-fixtures', fixtures.load_fixtures_from_json, name='load-fixtures'),
    path('api/load-results', fixtures.load_results_from_json, name='load-results'),
    path('api/responses', responses.receive_response, name='responses'),
    path('api/tally-responses', responses.tally_responses, name='tally_responses')
]
