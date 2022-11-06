from dataclasses import dataclass, field

import langcodes


@dataclass
class Card:
    """Deck representation class"""
    front: str
    back: str
    deck_name: str
    audio: None | str = None
    image: None | str = None
    tags: list[str] = field(default_factory=list)


def get_audio(lang_code: str, word: str):
    """Helper function for getting translated word audio"""
    return f'https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl={lang_code}&q={word}'


def get_langcode(natural_language_name: str) -> str | None:
    """Helper function for getting langcode"""
    language = langcodes.find(natural_language_name)
    return language.language
