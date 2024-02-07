import logging
import random
import time

from philosophers.abstract import AbstractPhilosopher
from enums import Side

logger = logging.getLogger(__name__)


class SmartPhilosopher(AbstractPhilosopher):
    """Represents thinker man."""

    def process(self) -> None:
        """Start dine."""
        logger.info(f"{self} join the table")

        while self.is_hungry:
            self._get_both_fork()
            self._eat()
            self._return_both_fork()

        logger.info(f"{self} left the table")

    def _get_both_fork(self) -> None:
        """Get fork from side."""
        time.sleep(random.random())
        got_left: bool = False
        got_right: bool = False

        while not (got_left and got_right):
            got_left: bool = self.forks[Side.LEFT].acquire(blocking=False)
            got_right: bool = self.forks[Side.RIGHT].acquire(blocking=False)

            if not (got_left and got_right):

                if got_left:
                    self.forks[Side.LEFT].release()

                if got_right:
                    self.forks[Side.RIGHT].release()
            time.sleep(random.random())
        logger.info(f"{self} get both forks from the table.")

    def _return_both_fork(self) -> None:
        """Return fork back."""
        self.forks[Side.LEFT].release()
        self.forks[Side.RIGHT].release()
        logger.info(f"{self} return both forks to the.")
        time.sleep(random.random())