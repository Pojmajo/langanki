import gspread

from libs.common import Card, get_audio, get_langcode
from libs.importers.common import Importer


class GoogleSheetsImporter(Importer):
    """Google sheets base class"""

    def __init__(self, spread_sheet_name='langanki'):
        self.google_service_account = gspread.service_account()
        self.langanki_sheet = self.google_service_account.open(spread_sheet_name)
        self.language_worksheets = self.langanki_sheet.worksheets()

    def import_cards(self) -> list[Card]:
        """Importing cards from Google Worksheets"""
        cards = []
        for worksheet in self.language_worksheets:
            lang_code = get_langcode(worksheet.title)
            for front, back in zip(worksheet.col_values(1), worksheet.col_values(2)):
                card = Card(front, back, worksheet.title)
                if lang_code is not None:
                    card.audio = get_audio(lang_code, back)
                cards.append(card)
        return cards
