from data.models import (
    CycleCount,
    Inventory
)

from sqlalchemy import func


class KPIService:

    @staticmethod
    def inventory_accuracy():

        counts = CycleCount.query.all()

        if not counts:
            return 100

        correct = len(
            [
                c for c in counts
                if c.variance == 0
            ]
        )

        return round(
            (correct / len(counts)) * 100,
            2
        )

    @staticmethod
    def inventory_units():

        result = Inventory.query.with_entities(
            func.sum(
                Inventory.quantity
            )
        ).scalar()

        return result or 0
