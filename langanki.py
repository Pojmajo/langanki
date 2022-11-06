import argparse

from libs.exporters.anki import AnkiExporter
from libs.importers import get_importer, ImporterName


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Welcome to langanki!')
    parser.add_argument("-i", "--importer", choices=['google'], required=True, type=str, help="Importer for Cards")

    args = parser.parse_args()
    importer = get_importer(ImporterName(args.importer))

    cards = importer.import_cards()

    anki_exporter = AnkiExporter()
    anki_exporter.export(cards)
