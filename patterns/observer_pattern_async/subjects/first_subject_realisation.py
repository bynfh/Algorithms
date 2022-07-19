from typing import List

from patterns.observer_pattern_async.observer_base import ObserverBase
from patterns.observer_pattern_async.subject_base import SubjectBase


class FirstRealisationSubject(SubjectBase):
    subscribers: List[ObserverBase] = []

    def subscribe(self, observers: List[ObserverBase]):
        self.subscribers.extend(observers)

    def unsubscribe(self, observer: ObserverBase):
        try:
            self.subscribers.remove(observer)
        except ValueError:
            print("Такого подписчика нет")

    def notify(self, value: str):
        for subscriber in self.subscribers:
            subscriber.update(value)
