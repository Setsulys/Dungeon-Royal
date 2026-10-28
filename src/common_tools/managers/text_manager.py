import yaml
from enum import Enum

from common_tools.managers.ressource_path import RESOURCES_DIR

LANGUAGES_DIR = RESOURCES_DIR / "languages"

class TextLanguage(Enum):
    FR="fr"
    EN="en"

class TextKey(Enum):
    GAME_TITLE = "game:title"
    GAME_MAIN_NEW_GAME = "game:main:new_game"
    GAME_MAIN_LOAD = "game:main:load"
    GAME_MAIN_SETTING = "game:main:settings"
    GAME_MAIN_LEAVE = "game:main:leave"
    GAME_CONFIRMATION_MESSAGE = "game:confirmation_message"



class TextManager:
        def __init__(self,language:TextLanguage=TextLanguage.EN):
            self.language=language
            self.texts={}
            self.load_language(language.value)

        def load_language(self,language:str)->None:
            path = LANGUAGES_DIR / f"{language}.yaml"

            self.texts = yaml.safe_load(
                path.read_text(encoding="utf-8")
            )

        def get(self,key:TextKey,**kwargs)->str:
            value = self.texts

            for part in key.value.split(":"):
                value = value[part]
            return value.format(**kwargs)
