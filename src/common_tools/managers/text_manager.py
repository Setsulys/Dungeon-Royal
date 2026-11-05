import yaml
from enum import Enum
from typing import Union

from common_tools.managers.ressource_path import RESOURCES_DIR
from common_tools import GAME_LANGUAGE

LANGUAGES_DIR = RESOURCES_DIR / "languages"



class TextLanguage(Enum):
    FR="fr"
    EN="en"

class TextKey(Enum):
    GAME_TITLE = "game:title"
    GAME_CONFIRMATION_MESSAGE = "game:confirmation_message"

class TextMainButton(Enum):
    NEW_GAME = "game:main:new_game"
    LOAD = "game:main:load"
    SETTING = "game:main:settings"
    LEAVE = "game:main:leave"

class TextManager:
        def __init__(self,language:TextLanguage=TextLanguage.EN):
            self.language=self.load_language(language.value)
            self.texts={}

        def load_language(self,language:str)->None:
            path = LANGUAGES_DIR / f"{language}.yaml"

            self.texts = yaml.safe_load(
                path.read_text(encoding="utf-8")
            )

        def get(self,key:Union[TextKey,TextMainButton],**kwargs)->str:
            value = self.texts

            for part in key.value.split(":"):
                value = value[part]
            return value.format(**kwargs)

        def set_language(self,new_language: TextLanguage):
            self.language = new_language
            self.load_language(new_language.value)


def language_setting(language : TextLanguage)-> None:
    GAME_LANGUAGE.set_language(language)
