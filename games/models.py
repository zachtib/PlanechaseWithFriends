from django.db import models
from uuid import uuid4, UUID

from base64 import urlsafe_b64decode, urlsafe_b64encode

from django.urls import reverse


def uuid_from_b64(b64string: str) -> UUID:
    return UUID(bytes=urlsafe_b64decode(b64string.encode() + b'=='))


def b64_from_uuid(uuid: UUID) -> str:
    return urlsafe_b64encode(uuid.bytes).removesuffix(b'==').decode()


class GameManager(models.Manager):

    def get_from_b64string(self, b64string: str) -> 'Game':
        decoded_uuid = uuid_from_b64(b64string)
        return self.get_queryset().get(uuid=decoded_uuid)


class Game(models.Model):
    uuid = models.UUIDField(unique=True, db_index=True, default=uuid4)

    objects = GameManager()

    def get_absolute_url(self):
        return reverse('games:room', kwargs={
            'game_id': self.get_b64string()
        })

    def get_b64string(self):
        return b64_from_uuid(self.uuid)

    def __str__(self):
        return f'Game(url={self.get_b64string()})'
