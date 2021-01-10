from django.test import TestCase

from .models import Game, uuid_from_b64, b64_from_uuid
from uuid import UUID


class UuidConversionTestCase(TestCase):

    def test_conversion_to_b64string(self):
        uuid = UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce')
        result = b64_from_uuid(uuid)
        self.assertIsNotNone(result)
        self.assertEqual('fvmtPUiXRjuG-yYgc4x5zg', result)

    def test_conversion_to_uuid(self):
        b64string = 'fvmtPUiXRjuG-yYgc4x5zg'
        result = uuid_from_b64(b64string)
        expected = UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce')
        self.assertEqual(result, expected)

    def test_b64string_strips_equals(self):
        uuid = UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce')
        result = b64_from_uuid(uuid)
        self.assertFalse(result.endswith('=='), 'Encoded strings are meant to strip == suffix')


class GamesTestCase(TestCase):

    def test_game_creation(self):
        game = Game.objects.create()
        self.assertTrue(str(game).startswith('Game(url='))

    def test_loading_game_by_b64string(self):
        game = Game.objects.create(uuid=UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce'))
        loaded_game = Game.objects.get_from_b64string('fvmtPUiXRjuG-yYgc4x5zg')
        self.assertEqual(game, loaded_game)

    def test_loading_invalid_b64string_throws(self):
        # noinspection PyTypeChecker
        with self.assertRaises(Game.DoesNotExist, msg=''):
            Game.objects.get_from_b64string('WNItBSfcR4unXjIglxnFDA')

    def test_game_get_b64string_method(self):
        game = Game.objects.create(uuid=UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce'))
        self.assertEqual('fvmtPUiXRjuG-yYgc4x5zg', game.get_b64string())

    def test_get_absolute_url(self):
        game = Game.objects.create(uuid=UUID('7ef9ad3d-4897-463b-86fb-2620738c79ce'))
        actual = game.get_absolute_url()
        self.assertEqual('/games/fvmtPUiXRjuG-yYgc4x5zg/', actual)
