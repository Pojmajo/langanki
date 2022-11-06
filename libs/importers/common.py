import abc

from libs.common import Card


class Importer(abc.ABC):
    """Importer base class"""

    @abc.abstractmethod
    def import_cards(self) -> list[Card]:
        """
        Import cards from Google Sheets

        :return: List of Card objects
        """
        pass
