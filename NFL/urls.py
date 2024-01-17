from django.urls import path
from NFL.views import fixtures

urlpatterns = [
    path('fixtures', fixtures.getFixtures, name='fixtures'),
    path('results', fixtures.getResults, name='results'),
]
