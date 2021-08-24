from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import ReviewForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# class Game:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, genre, description, dateReleased):
#     self.name = name
#     self.genre = genre
#     self.description = description
#     self.dateReleased = dateReleased

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('games_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = "/games/"

games = [
  Game('MW2', 'shooter', 'Fun shooter', 2009),
  Game('La Noire', 'Crime', 'Fun Crime game from 40s', 2012),
  Game('Black Ops', 'Shooter', 'Cold War era shooter', 2010),
  Game('AC: Valhalla', 'Adventure', 'Viking Assassins', 2020)
]

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  review_form = ReviewForm()
  return render(request, 'games/detail.html', { 
    'game': game, 
    'review_form': review_form 
    })

@login_required
def add_review(request, game_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.game_id = game_id
    new_review.save()
  return redirect('games_detail', game_id=game_id)
