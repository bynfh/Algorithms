from patterns.singletone.impl_singletone import SingletonMeta


class DataBase(metaclass=SingletonMeta):
    """Это потокобезопасная реализация класса Singleton."""

    value: str = None

    def __init__(self, value: str):
        self.value = value

    def select(self):
        return f"select from db: {self.value}"

    def __repr__(self):
        return f"{self.value=}"
