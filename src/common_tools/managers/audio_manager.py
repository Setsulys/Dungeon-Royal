from time import sleep

import pygame
from enum import Enum,auto
from pathlib import Path

from common_tools.managers.ressource_path import RESOURCES_DIR

AUDIO_DIR = RESOURCES_DIR / "audios"

MUSIC_DIR = AUDIO_DIR / "musics"

SOUND_DIR = AUDIO_DIR / "sounds"

class Volume(Enum):
    UP=auto()
    DOWN=auto()


class AudioManager:
    def __init__(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        self.master_volume=1.0
        self.music_volume=0.5
        self.sound_volume=0.5
        self.is_paused = True
        self.sounds: list[pygame.mixer.Sound]=[]
        self._apply_music_volume()


    def _adjust_volume(self,current:float,direction:Volume)->float:
        delta = 0.1 if direction == Volume.UP else -0.1
        return round(min(1.0,max(0.0,current+delta)),1)

    def _apply_music_volume(self)->None:
        volume = self.master_volume*self.music_volume
        pygame.mixer.music.set_volume(volume)

    def _apply_sound_volume(self) -> None:
        volume = self.master_volume * self.sound_volume
        for sound in self.sounds:
            sound.set_volume(volume)

    def adjust_master_volume(self, direction: Volume) -> None:
        self.master_volume = self._adjust_volume(
            self.master_volume, direction
        )
        self._apply_music_volume()
        self._apply_sound_volume()

    def adjust_music_volume(self, direction: Volume) -> None:
        self.music_volume = self._adjust_volume(
            self.music_volume, direction
        )
        self._apply_music_volume()

    def adjust_sound_volume(self, direction: Volume) -> None:
        self.sound_volume = self._adjust_volume(
            self.sound_volume, direction
        )
        self._apply_sound_volume()

    def play_music(self, path: str | Path) -> None:
        pygame.mixer.music.load(path)
        self._apply_music_volume()
        pygame.mixer.music.play(-1)
        self.is_paused=False

    def toggle_music_pause(self) -> None:
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.is_paused= not self.is_paused


    def play_sound(self, path: str | Path) -> None:
        sound = pygame.mixer.Sound(path)
        self.sounds.append(sound)
        sound.set_volume(self.master_volume * self.sound_volume)
        sound.play()


if __name__ == "__main__":
    path = MUSIC_DIR/ "Life Will Change.mp3"
    audio_manager = AudioManager()
    audio_manager.play_music(path)
    #
    # sleep(5)
    # audio_manager.adjust_music_volume(Volume.UP)
    # sleep(1)
    # audio_manager.adjust_music_volume(Volume.UP)
    # sleep(1)
    # audio_manager.adjust_music_volume(Volume.UP)
    # sleep(1)
    # audio_manager.adjust_music_volume(Volume.UP)

    input("Musique en cours... Appuie sur Entrée pour quitter.")
    pygame.quit()