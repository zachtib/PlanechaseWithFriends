from django.http import Http404
from django.shortcuts import render, redirect

from games.models import Game
from planes.models import PlanarCard


def index(request):
    return render(request, 'games/index.html')


def create(request):
    new_game: Game = Game.objects.create()
    return redirect('games:room', game_id=new_game.get_b64string())


def room(request, game_id):
    try:
        game = Game.objects.get_from_b64string(game_id)
    except Game.DoesNotExist:
        raise Http404()
    card: PlanarCard = PlanarCard.objects.first()
    return render(request, 'games/room.html', {
        'room_id': game.get_b64string(),
        'img_placeholder': card.image_url,
    })
