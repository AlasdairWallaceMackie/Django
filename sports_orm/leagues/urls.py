from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('initialize', views.make_data, name="make_data"),
	path('baseball_leagues', views.baseball_leagues),
	path('womens_leagues', views.womens_leagues),
	path('hockey_type_leagues', views.hockey_type_leagues),
	path('leagues_except_football', views.leagues_except_football),
	path('conference_leagues', views.conference_leagues),
	path('atlantic_leagues', views.atlantic_leagues),
	path('dallas_teams', views.dallas_teams),
	path('raptor_teams', views.raptor_teams),
	path('city_teams', views.city_teams),
	path('teams_startswith_t', views.teams_startswith_t),
	path('allteams_alphabetical_location', views.allteams_alphabetical_location),
	path('allteams_reverse_alphabetical', views.allteams_reverse_alphabetical),
	path('lastname_cooper', views.lastname_cooper),
	path('firstname_joshua', views.firstname_joshua),
	path('cooper_no_joshua', views.cooper_no_joshua),
	path('alexander_or_wyatt', views.alexander_or_wyatt),
]
