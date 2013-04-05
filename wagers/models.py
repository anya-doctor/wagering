from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

class WagerSettingSingleton(models.Model):
    default_credits = models.DecimalField(decimal_places=10, max_digits=100, default=10)

    def save(self, *args, **kwargs):
        self.id = 1
        super(WagerSettingSingleton, self).save(*args, **kwargs)

    def delete(self):
        pass
        
class EditableHTML(models.Model):
    html = models.TextField()

class Wager(models.Model):
    is_open = models.BooleanField(default=True)
    winning_position = models.BooleanField(default=True) # winning_position means team_a won
    team_a = models.TextField()
    team_b = models.TextField()
    notes = models.TextField()
    
    def __str__(self):
      return self.team_a + " vs " + self.team_b

class Bet(models.Model): 
    amount_bet = models.DecimalField(decimal_places=10, max_digits=100)
    on_prop = models.ForeignKey("Wager")
    user = models.ForeignKey(User)
    position = models.BooleanField()

    class Meta():
        unique_together = [("user", "on_prop")]

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    credits = models.DecimalField(decimal_places=10, max_digits=100)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        wager_settings, created = WagerSettingSingleton.objects.get_or_create(id=1)
        profile, created = UserProfile.objects.get_or_create(user=instance, credits=wager_settings.default_credits)
        profile.save()

post_save.connect(create_user_profile, sender=User)


