from django.urls import path
from lipalater.views import lipalater_loans


urlpatterns = [
    path("", lipalater_loans, name="lipa-polepole-loans"),
]