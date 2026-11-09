from pathlib import Path

RESOURCES_DIR = (
        Path(__file__).parent.parent
        / "resources"
)

from managers.audio_manager import AudioManager
from managers.image_manager import ImageManager,read_image
from managers.text_manager import TextManager,TextKey,TextMainButton,TextLanguage

AUDIO = audio_manager.AudioManager()

__all__ =["AUDIO","AudioManager","ImageManager","TextManager","TextLanguage","TextMainButton","TextKey","read_image","RESOURCES_DIR"]



