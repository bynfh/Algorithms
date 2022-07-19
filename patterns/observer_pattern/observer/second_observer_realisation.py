from patterns.observer_pattern.observer_base import ObserverBase


class SecondRealisationObserver(ObserverBase):
    value: str = None
    changed: bool = False

    def update(self, value: str):
        self.value = value
        self._display()

    def _display(self):
        print(f"\nТекущие данные: {self.value}\nИмя объекта:{self.__class__.__name__}")
