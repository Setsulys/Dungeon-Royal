from . import text_manager
from . import image_manager
from . import audio_manager
from . import ressource_path

__all__ =["text_manager","image_manager","audio_manager","ressource_path","AUDIO",]

AUDIO = audio_manager.AudioManager()
