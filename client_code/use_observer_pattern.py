import random
import time

from patterns.observer_pattern.observer.first_observer_realisation import FirstRealisationObserver
from patterns.observer_pattern.observer.second_observer_realisation import SecondRealisationObserver
from patterns.observer_pattern.subject_base import SubjectBase
from patterns.observer_pattern.subjects.first_subject_realisation import FirstRealisationSubject

values = [str(i) for i in range(100)]


def imitate_changes(subject: SubjectBase):
    """Имитация изменения в subject."""
    time.sleep(1)
    subject.notify(random.choice(values))


def client_code():
    subject = FirstRealisationSubject()

    first_observer = FirstRealisationObserver()
    second_observer = SecondRealisationObserver()

    # Подписываем наблюдателей на рассылку
    subject.subscribe([first_observer, second_observer])

    # Имитируем изменение данных в  subject
    for _ in range(2):
        imitate_changes(subject)

    # Отписываем от рассылки наблюдателя
    subject.unsubscribe(first_observer)
    print(f"===== {first_observer.__class__.__name__} отписался от рассылки =====")

    # Имитируем изменение данных в  subject
    for _ in range(1):
        imitate_changes(subject)


if __name__ == "__main__":
    client_code()
