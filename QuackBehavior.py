# E22MCAG0004
# Md Najeebur Rahman
from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
