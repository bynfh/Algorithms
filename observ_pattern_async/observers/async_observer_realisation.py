import asyncio

from ObserverPattern.observer_base import ObserverBase


class AsyncRealisationObserver(ObserverBase):
    previous_value: str = None
    value: str = None
    changed: bool = False

    def update(self, value: str):
        if self.value:
            self.previous_value = self.value
        self.value = value
        self.changed = True

    async def display(self):
        if self.changed:
            print(f"Я Умная функция отслеживаю изменения."
                  f" Текущие данные: {self.value} Имя объекта:{self.__class__.__name__}")

            self.changed = False


