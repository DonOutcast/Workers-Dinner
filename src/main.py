import logging

from service import start_dinner
from tables import (
    Table,
    TableWithNumberedForks,
    TableWithSmartPhilosophers,
    TableWithWaiter,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    # start_dinner(Table)
    # start_dinner(TableWithSmartPhilosophers)
    # start_dinner(TableWithWaiter)
    start_dinner(TableWithNumberedForks)
