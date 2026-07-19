from models import (
    CycleCount,
    InventoryTransaction,
    db
)


class CycleCountService:

    @staticmethod
    def create_count(
        sku,
        location,
        expected_qty,
        counted_qty,
        user
    ):

        variance = counted_qty - expected_qty

        count_record = CycleCount(
            sku=sku,
            location=location,
            expected_qty=expected_qty,
            counted_qty=counted_qty,
            variance=variance,
            counted_by=user
        )

        db.session.add(count_record)

        audit = InventoryTransaction(
            sku=sku,
            location=location,
            quantity=counted_qty,
            transaction_type="CYCLE_COUNT",
            note=f"Variance: {variance}"
        )

        db.session.add(audit)

        db.session.commit()

        return count_record
