import logging
import random
import time
from abc import ABC, abstractmethod
from threading import Thread

from enums import Side
from forks import Fork

logger = logging.getLogger(__name__)


class AbstractPhilosopher(Thread, ABC):
    """Abstract thinker man."""

    def __init__(
        self,
        name: str,
        left_fork: Fork,
        right_fork: Fork,
    ):
        super().__init__(name=name, target=self.process)
        self.forks: dict[Side, Fork] = {
            Side.LEFT: left_fork,
            Side.RIGHT: right_fork,
        }
        self.is_hungry: bool = True

    @abstractmethod
    def process(self):
        """Start dine."""

    def _eat(self) -> None:
        """Eat for a while."""
        logger.info(f"{self} began to eat")
        time.sleep(5)
        logger.info(f"{self} finished eating")
        time.sleep(random.random())

    def __repr__(self):
        return f"<Philosopher {self.name}>"