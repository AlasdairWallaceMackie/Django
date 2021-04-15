from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from itertools import chain

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

def team_info(request, team_name):
	context = {
		'team': Team.objects.get(team_name = team_name)
	}
	return render(request, 'leagues/team_info.html', context)

def league_info(request, league_name):
	context = {
		'league': League.objects.get(name = league_name)
	}	
	return render(request, 'leagues/league_info.html', context)

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

def twelve_or_more_players(request):
	all_teams = Team.objects.annotate( number_of_players = Count('all_players') )
	all_teams = all_teams.filter( number_of_players__gt = 12 )
	context = {
		'teams': all_teams,
	}
	return render(request, 'leagues/index.html', context)

def teams_with_sophia(request):
	context = {
		'teams': Team.objects.filter( curr_players__first_name__contains="Sophia")
	}

	return render(request, 'leagues/index.html', context)

def all_football_players(request):
	context = {
		'players': Player.objects.filter( curr_team__league__sport="Football" )
	}
	return render(request, 'leagues/index.html', context)