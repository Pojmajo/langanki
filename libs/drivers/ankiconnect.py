import enum
import json
import logging
from http import HTTPStatus
from json import JSONDecodeError

import requests

from libs.common import Card

LOCALHOST = r'http://localhost:8765'


class Action(enum.Enum):
    """Available actions"""

    DECK_NAMES = 'deckNames'
    CREATE_DECK = 'createDeck'
    ADD_NOTES = 'addNotes'
    SYNC = 'sync'


class AnkiConnectDriver:
    """Driver for handling AnkiConnect"""

    ANKI_CONNECT_VERSION = 6

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._is_context_manager = False

    def request(self, action: Action, **params):
        """Returns AnkiConnect request"""
        return {
            'action': action.value,
            'version': self.ANKI_CONNECT_VERSION,
            'params': params
        }

    def invoke_command(self, action: Action, **params):
        """Invoke AnkiConnect command"""
        if not self._is_context_manager:
            raise EnvironmentError('This class is supposed to be run within ContextManager')

        request = json.dumps(self.request(action, **params)).encode('utf-8')
        response = requests.post(LOCALHOST, request, timeout=15)
        if response.status_code != HTTPStatus.OK:
            raise InterruptedError('Cannot connect to localhost')

        try:
            response = json.loads(response.text)
        except JSONDecodeError as error:
            self.logger.error(
                'Error was found during converting json response to dict: %s', error.msg)
            return None, -1

        return response.get('result'), response.get('error', -1)

    def send_and_receive(self, action: Action, **params):
        """Send AnkiConnect request and receive response"""
        result, _ = self.invoke_command(action, **params)
        return result

    def send(self, action: Action, **params) -> bool:
        """Send AnkiConnect request"""
        _, error = self.invoke_command(action, **params)
        if error == -1 or error is not None:
            return False
        return True

    @property
    def deck_names(self) -> list[str]:
        """Returns deck names"""
        return self.send_and_receive(Action.DECK_NAMES)

    def sync(self) -> bool:
        """Synchronize the local Anki collections with AnkiWeb"""
        return self.send(Action.SYNC)

    def create_deck(self, deck_name: str) -> bool:
        """Creates deck with specified name"""
        if deck_name in self.deck_names:
            self.logger.info('Deck name: %s is already existing', deck_name)
            return True
        return self.send(Action.CREATE_DECK, deck=deck_name)

    @staticmethod
    def _prepare_card_params(card: Card) -> dict:
        """Helper method for preparing card params"""
        note = {
            'deckName': card.deck_name,
            'modelName': 'Basic',
            'fields': {
                'Front': card.front,
                'Back': card.back
            },
            "options": {
                "allowDuplicate": False,
                "duplicateScope": "deck",
                "duplicateScopeOptions": {
                    "deckName": card.deck_name,
                    "checkChildren": False,
                    "checkAllModels": False
                }
            }
        }
        if len(card.tags) != 0:
            note['tags'] = card.tags

        if card.audio is not None:
            note['audio'] = [
                {
                    "url": card.audio,
                    "filename": f"{card.back.encode('ascii', errors='ignore').decode()}.mp3",
                    "fields": ['Back']
                }
            ]
        return note

    def add_cards(self, cards: list[Card]) -> bool:
        """Add cards to specified decks"""
        cards_deck_names = {card.deck_name for card in cards}
        for deck_name in cards_deck_names:
            if deck_name not in self.deck_names:
                self.create_deck(deck_name)

        params = {"notes": [self._prepare_card_params(card) for card in cards]}
        return self.send(Action.ADD_NOTES, **params)

    def __enter__(self):
        self._is_context_manager = True
        # ToDo - here open Anki

    def __exit__(self, exception_type, exception_value, traceback):
        # ToDo - here close Anki
        self._is_context_manager = False
