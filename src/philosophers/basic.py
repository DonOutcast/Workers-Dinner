import logging
import random
import time

from philosophers.abstract import AbstractPhilosopher
from enums import Side

logger = logging.getLogger(__name__)


class Philosopher(AbstractPhilosopher):
    """Represents thinker man."""

    def process(self) -> None:
        """Start dine."""
        logger.info(f"{self} join the table")

        while self.is_hungry:
            self._get_fork(Side.LEFT)
            self._get_fork(Side.RIGHT)
            self._eat()
            self._return_fork(Side.RIGHT)
            self._return_fork(Side.LEFT)

        logger.info(f"{self} left the table")

    def _get_fork(self, side: Side) -> None:
        """Get fork from side."""
        fork = self.forks[side]
        fork.acquire()
        logger.info(f"{self} get {fork} from the {side}")
        time.sleep(random.random())

    def _return_fork(self, side: Side) -> None:
        """Return fork back."""
        fork = self.forks[side]
        fork.release()
        logger.info(f"{self} return fork {fork} to the {side}")
        time.sleep(random.random())
