from pathlib import Path

RESOURCES_DIR = (
        Path(__file__).parent.parent.parent
        / "resources"
)

from managers.audio_manager import AudioManager
from managers.image_manager import ImageManager,read_image,game_icon
from managers.text_manager import TextManager,TextKey,TextMainButton,TextLanguage
from managers.input_manager import Input, InputManager

AUDIO = audio_manager.AudioManager()

__all__ =["RESOURCES_DIR",
          "AUDIO","AudioManager",
          "ImageManager","read_image","game_icon",
          "TextManager","TextLanguage","TextMainButton","TextKey",
          "InputManager", "Input"]
