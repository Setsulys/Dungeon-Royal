from abc import ABC,abstractmethod


class Screen(ABC):

    @abstractmethod
    def handle_events(self,events):
        pass

    @abstractmethod
    def update(self,dt):
        pass

    @abstractmethod
    def draw(self,surface):
        pass

    def on_enter(self):
        """Appelé lorsque l'écran devient actif."""
    pass

    def on_exit(self):
        """Appelé lorsque l'écran cesse d'être actif."""
        pass

