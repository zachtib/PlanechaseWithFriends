from django.core.management import BaseCommand

from planes.models import PlanarCard
from planes.scryfall import get_all_planar_cards


class Command(BaseCommand):
    help = 'Updates the local cache from Scryfall'

    def handle(self, *args, **options):
        result = get_all_planar_cards()
        if result is None:
            raise Exception('Got an error from Scryfall API')
        PlanarCard.objects.load_from_api_response(result)
