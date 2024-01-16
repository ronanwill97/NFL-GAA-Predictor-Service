from django.urls import path
from views import fixtures, payments

urlpatterns = [
    path('fixtures', fixtures.getFixtures, name='fixtures'),
    path('results', fixtures.getResults, name='results'),
    path('payments', payments.create_payment, name='payments')
]
