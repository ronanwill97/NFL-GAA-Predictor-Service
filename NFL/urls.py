from django.urls import path
from NFL.views import fixtures

urlpatterns = [
    path('get-fixtures', fixtures.get_fixtures, name='get-fixtures'),
    path('load-fixtures', fixtures.load_fixtures_from_json, name='load-fixtures')
]
