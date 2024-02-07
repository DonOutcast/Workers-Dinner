from .abstract import AbstractPhilosopher
from .basic import Philosopher
from .smart import SmartPhilosopher
from .waiter import PhilosopherWithWaiter
from .numbered import PhilosopherWithNumberedForks


__all__ = [
    "AbstractPhilosopher",
    "Philosopher",
    "PhilosopherWithNumberedForks",
    "SmartPhilosopher",
    "PhilosopherWithWaiter",
]