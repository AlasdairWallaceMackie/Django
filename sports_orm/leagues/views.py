from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def baseball_leagues(request):
	context = {
		'leagues': League.objects.filter(sport="Baseball")
	}
	return render(request, "leagues/index.html", context)

def womens_leagues(request):
	context = {
		'leagues': League.objects.filter(name__contains="Womens")
	}
	return render(request, "leagues/index.html", context)

def hockey_type_leagues(request):
	context = {
		'leagues': League.objects.filter(name__contains="Hockey")
	}
	return render(request, "leagues/index.html", context)

def leagues_except_football(request):
	context = {
		'leagues': League.objects.exclude(sport="Football")
	}
	return render(request, "leagues/index.html", context)

def conference_leagues(request):
	context = {
		'leagues': League.objects.filter(name__contains="Conference")
	}
	return render(request, "leagues/index.html", context)

def atlantic_leagues(request):
	context = {
		'leagues': League.objects.filter(name__contains="Atlantic")
	}
	return render(request, "leagues/index.html", context)

def dallas_teams(request):
	context = {
		'teams': Team.objects.filter(location="Dallas")
	}
	return render(request, "leagues/index.html", context)

def raptor_teams(request):
	context = {
		'teams': Team.objects.filter(team_name="Raptors")
	}
	return render(request, "leagues/index.html", context)

def city_teams(request):
	context = {
		'teams': Team.objects.filter(location__contains="City")
	}
	return render(request, "leagues/index.html", context)

def teams_startswith_t(request):
	context = {
		'teams': Team.objects.filter(team_name__startswith="T")
	}
	return render(request, "leagues/index.html", context)

def allteams_alphabetical_location(request):
	context = {
		'teams': Team.objects.order_by('location')
	}
	return render(request, "leagues/index.html", context)

def allteams_reverse_alphabetical(request):
	context = {
		'teams': Team.objects.order_by('-location')
	}
	return render(request, "leagues/index.html", context)

def lastname_cooper(request):
	context = {
		'players': Player.objects.filter(last_name="Cooper")
	}
	return render(request, "leagues/index.html", context)

def firstname_joshua(request):
	context = {
		'players': Player.objects.filter(first_name="Joshua")
	}
	return render(request, "leagues/index.html", context)

def cooper_no_joshua(request):
	context = {
		'players': Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
	}
	return render(request, "leagues/index.html", context)

def alexander_or_wyatt(request):
	context = {
		'players': Player.objects.filter( Q(first_name="Alexander") | Q(first_name="Wyatt"))
	}
	return render(request, "leagues/index.html", context)
