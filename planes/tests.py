import responses
from django.test import TestCase

from . import scryfall, test_data


class ScryfallTestCase(TestCase):

    def test_getting_planes(self):
        with responses.RequestsMock() as rm:
            rm.add('GET', test_data.URL, body=test_data.PLANES_RESPONSE)
            cards = scryfall.get_all_planar_cards()
            self.assertEqual(3, len(cards))
            card: scryfall.ScryfallApiPlanarCard = cards[0]
            self.assertEqual('Academy at Tolaria West', card.name)
            self.assertEqual('Plane — Dominaria', card.type_line)
            self.assertEqual('At the beginning of your end step, if you have no cards in hand, draw seven '
                             'cards.\nWhenever you roll {CHAOS}, discard your hand.', card.oracle_text)

    def test_non_200_response(self):
        with responses.RequestsMock() as rm:
            rm.add('GET', test_data.URL, status=502)
            cards = scryfall.get_all_planar_cards()
            self.assertIsNone(cards)
