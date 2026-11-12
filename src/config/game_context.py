from typing import Union
from managers import TextManager, TextLanguage,TextKey,TextMainButton

class GameContext:

    def __init__(self):
        self.available_languages={
            language:TextManager(language) for language in TextLanguage
        }
        self.current_language = TextLanguage.FR
        self.text_manager = self.available_languages[TextLanguage.FR]

    def change_language(self, language:TextLanguage)-> None:
        self.current_language = language
        self.text_manager = self.available_languages[language]

    def read(self,key:Union[TextKey,TextMainButton],**kwargs):
        return self.text_manager.get(key)