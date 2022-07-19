import random
from asyncio import get_event_loop, sleep, gather

from patterns.observer_pattern_async.observers.async_observer_realisation import AsyncRealisationObserver
from patterns.observer_pattern_async.observers.async_second_observer_realisation import AsyncSecondRealisationObserver
from patterns.observer_pattern_async.subject_base import SubjectBase
from patterns.observer_pattern_async.subjects.first_subject_realisation import FirstRealisationSubject

values = [str(random.randint(-30, i)) for i in range(30)]


async def imitate_changes(subject_inner: SubjectBase):
    """Имитация изменения в subject."""
    while True:
        response = input("Хотите имитировать изменения погоды? Да или нет:").lower()
        if response in ["y", "yes", "да", "д"]:
            subject_inner.notify(random.choice(values))
        await sleep(0.1)


async def first_display():
    """Выводит на дисплей значение потом спит 2 секунды."""
    while True:
        await first_observer.display()
        await sleep(2)


async def second_display():
    """Выводит на дисплей значение потом спит 2 секунды."""
    while True:
        await second_observer.display()
        await sleep(2)


if __name__ == "__main__":
    # Инициализация
    subject = FirstRealisationSubject()
    first_observer = AsyncRealisationObserver()
    second_observer = AsyncSecondRealisationObserver()
    subject.subscribe([first_observer, second_observer])

    loop = get_event_loop()
    loop.run_until_complete(gather(imitate_changes(subject), first_display(), second_display()))
