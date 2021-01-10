from typing import Optional

from django.db import models
from .scryfall import ScryfallApiPlanarCard


def select_best_image_uri(images: dict) -> Optional[str]:
    for key in ('png', 'large', 'normal', 'small'):
        if key in images.keys():
            return images[key]
    return None


def planar_card_from_api_object(data: ScryfallApiPlanarCard) -> 'PlanarCard':
    return PlanarCard(
        scryfall_id=data.id,
        name=data.name,
        type_line=data.type_line,
        oracle_text=data.oracle_text,
        image_url=select_best_image_uri(data.image_uris)
    )


class PlanarCardManager(models.Manager):

    def load_from_api_response(self, cards):
        self.get_queryset().delete()
        new_cards = [planar_card_from_api_object(card) for card in cards]
        PlanarCard.objects.bulk_create(new_cards)


class PlanarCard(models.Model):
    scryfall_id = models.UUIDField(unique=True)
    name = models.CharField(max_length=100)
    type_line = models.CharField(max_length=100)
    oracle_text = models.TextField()
    image_url = models.URLField()

    objects = PlanarCardManager()

    def __str__(self):
        return self.name
