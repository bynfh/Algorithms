from abc import ABC, abstractmethod
from typing import List

from ObserverPattern.observer_base import ObserverBase


class SubjectBase(ABC):
    @abstractmethod
    def subscribe(self, observers: List[ObserverBase]):
        raise NotImplementedError()

    @abstractmethod
    def unsubscribe(self, observer: ObserverBase):
        raise NotImplementedError()

    @abstractmethod
    def notify(self, value: str):
        raise NotImplementedError()
