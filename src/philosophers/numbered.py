import logging

from philosophers.basic import Philosopher


logger = logging.getLogger(__name__)


class PhilosopherWithNumberedForks(Philosopher):

    def process(self) -> None:
        logger.info(f"{self} join the table")
        sides_ordered = [
            side for side, _ in sorted(self.forks.items(), key=lambda item: item[1].id)
        ]

        while self.is_hungry:
            for side in sides_ordered:
                self._get_fork(side)

            self._eat()

            for side in sides_ordered:
                self._return_fork(side)

        logger.info(f"{self} left the table")
