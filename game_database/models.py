from django.db import models

class Game(models.Model):
	game_type = models.CharField(max_length=10)
	start_time = models.DateTimeField()
	
	team_a = models.CharField(max_length=80)
	team_a_aux_info_1 = models.CharField(max_length=144)
	team_a_score = models.IntegerField(null=True)

	team_b = models.CharField(max_length=80)
	team_b_aux_info_1 = models.CharField(max_length=144)
	team_b_score = models.IntegerField(null=True)

	is_finished = models.BooleanField()
	# Won if team a wins, Lost if team b wins, Drawn if a draw, N/A if not finished
	outcome = models.CharField(max_length=5, blank=True)

	def __str__(self):
		return self.team_a + " vs " + self.team_b
		
	
	def update(self, game):
		self.game_type = game['game_type']
		self.start_time = game['start_time']
		self.team_a = game['team_a']
		self.team_a_aux_info_1 = game['team_a_aux_1']
		self.team_a_score = game['team_a_score']
		self.team_b = game['team_b']
		self.team_b_aux_info_1 = game['team_b_aux_1']
		self.team_b_score = game['team_b_score']
		self.is_finished = game['is_finished']
		self.outcome = game['outcome']
		self.save()
