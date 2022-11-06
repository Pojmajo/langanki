import logging
import time

from libs.common import Card
from libs.drivers.ankiconnect import AnkiConnectDriver
from libs.exporters.common import Exporter


class AnkiExporter(Exporter):
    """AnkiExporter. Exports Decks to Anki"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.sync_delay = 5
        self._driver = AnkiConnectDriver()
        self._driver.__enter__()

    def export(self, cards: list[Card]) -> bool:
        """Exporting cards to Anki"""
        add_result = self._driver.add_cards(cards)
        sync_result = self._driver.sync()
        self.logger.info('Wait 5s to let Anki synchronize with AnkiWeb')
        time.sleep(self.sync_delay)
        return all((add_result, sync_result))

    def __del__(self):
        self._driver.__exit__(None, None, None)
        del self
