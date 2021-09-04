from ObserverPattern.observer_base import ObserverBase


class FirstRealisationObserver(ObserverBase):
    previous_value: str = None
    value: str = None
    changed: bool = False

    def update(self, value: str):
        if self.value:
            self.previous_value = self.value
        self.value = value
        self._display()

    def _display(self):
        if not self.previous_value:
            self.previous_value = "Отсутствуют"
        print(f"Мы отображаем данные, так как они изменились.\nПредыдущие данные:{self.previous_value}"
              f"\nТекущие данные: {self.value}\nИмя объекта:{self.__class__.__name__}")
