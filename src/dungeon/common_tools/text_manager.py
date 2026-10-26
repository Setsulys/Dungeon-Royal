import yaml
from pathlib import Path

class TextManager:
        def __init__(self,language: str="en"):
            self.language=language
            self.texts={}
            self.load_language(language)

        def load_language(self,language:str)->None:
            path = Path(__file__).parent.parent.parent / "locales" / f"{language}.yaml"

            self.texts = yaml.safe_load(
                path.read_text(encoding="utf-8")
            )

        def get(self,key:str,**kwargs)->str:
            value = self.texts

            for part in key.split("."):
                value=value[part]
            return value.format(**kwargs)
