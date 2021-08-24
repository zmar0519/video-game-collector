from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

RATINGS = (
  ('1', '1 Star'),
  ('2', '2 Stars'),
  ('3', '3 Stars'),
  ('4', '4 Stars'),
  ('5', '5 Stars'),
)

class Game(models.Model):
  name = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  releaseDate = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Reviews(models.Model):
  name = models.CharField(max_length=20)
  rating = models.CharField(
    max_length=1,
    choices=RATINGS,
    default=RATINGS[0][0]
  )

  Game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_rating_display()} rating"

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("games_detail", kwargs={"game_id": self.id})
  