from celery import task
from game_database.models import Game
from game_database.scraper import get_games_on
import datetime
from django.utils import timezone

def update_db_from(game):
	try:
		db_game = Game.objects.get(start_time=game["start_time"], team_a=game["team_a"], team_b=game["team_b"])
	except:
		db_game = Game()
	db_game.update(game)

@task()
def scrape_mlb():
	today = timezone.now()
	days = [today, today-datetime.timedelta(days=1), today-datetime.timedelta(days=2)]
	for day in days:
		games = get_games_on(day)
		for game in games:
			update_db_from(game)

