from patterns.observer_pattern_async.observer_base import ObserverBase


class AsyncSecondRealisationObserver(ObserverBase):
    value: str = None
    changed: bool = False

    def update(self, value: str):
        self.value = value

    async def display(self):
        print(
            f"Я Тупая функция не отслеживаю изменения, текущие данные: "
            f"{self.value} Имя объекта:{self.__class__.__name__}",
        )
