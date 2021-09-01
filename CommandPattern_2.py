"""Example command pattern version 2"""
from typing import Optional


class Command:

    def execute(self):
        raise NotImplementedError()


class SimpleCommand(Command):

    def __init__(self, payload: Optional[str] = None):
        self._payload = payload

    def execute(self):
        if self._payload:
            print(f"It's simple command for print payload:{self._payload}")
            return
        print("It's simple command")


class ComplexCommand(Command):
    """
    Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемым «получателями».
    """

    def __init__(self, receiver: "Receiver", a: str, b: str) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Команды могут делегировать выполнение любым методам получателя.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="\n")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    Классы Получателей содержат некую важную бизнес-логику. Они умеют выполнять
    все виды операций, связанных с выполнением запроса. Фактически, любой класс
    может выступать Получателем.
    """

    @staticmethod
    def do_something(a: str) -> None:
        print(f"Receiver: Working on ({a})", end="\n")

    @staticmethod
    def do_something_else(b: str) -> None:
        print(f"Receiver: Also working on ({b})", end="\n")


def client_code():
    command_first = SimpleCommand()
    command_first.execute()
    receiver = Receiver()
    command_second = ComplexCommand(receiver, "1", "2")
    command_second.execute()


if __name__ == "__main__":
    client_code()
