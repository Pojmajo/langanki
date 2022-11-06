import enum

from libs.importers.google_sheets import GoogleSheetsImporter


class ImporterName(enum.Enum):
    """Importer Names"""

    GOOGLE_SHEETS = 'google'
    UNSUPPORTED = 'unsupported'

    @classmethod
    def _missing_(cls, value):
        return cls.UNSUPPORTED


def get_importer(importer_name: ImporterName):
    """Function for getting deck importers"""
    match importer_name:
        case ImporterName.GOOGLE_SHEETS:
            return GoogleSheetsImporter()
    raise ValueError('There is no such importer supported!')
