import yaml
from enum import Enum
from typing import Union
from managers import RESOURCES_DIR


LANGUAGES_DIR = RESOURCES_DIR / "languages"


class TextLanguage(Enum):
    FR="fr"
    EN="en"
    DE="de"


class TextKey(Enum):
    GAME_TITLE = "game:title"
    GAME_CONFIRMATION_MESSAGE = "game:confirmation_message"

class TextMainButton(Enum):
    NEW_GAME = "game:main:new_game"
    LOAD = "game:main:load"
    SETTING = "game:main:settings"
    LEAVE = "game:main:leave"

class TextManager:
        def __init__(self,language:TextLanguage= TextLanguage.EN):
            self.language=language
            self.texts={}
            self.load_language(language.value)

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


