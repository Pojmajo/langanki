import abc

from libs.common import Card


class Exporter(abc.ABC):
    """Exporter base class"""

    @abc.abstractmethod
    def export(self, cards: list[Card]) -> bool:
        """
        Exports decks.

        :param cards: List of decks
        :return: True if successfully exported
        """
        pass
