from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CycleCount(db.Model):
    __tablename__ = "cycle_counts"

    id = db.Column(db.Integer, primary_key=True)

    sku = db.Column(db.String(50), nullable=False)

    location = db.Column(
        db.String(50),
        nullable=False
    )

    expected_qty = db.Column(
        db.Integer,
        nullable=False
    )

    counted_qty = db.Column(
        db.Integer,
        nullable=False
    )

    variance = db.Column(
        db.Integer,
        nullable=False
    )

    counted_by = db.Column(
        db.String(100)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


class InventoryTransaction(db.Model):
    __tablename__ = "inventory_transactions"

    id = db.Column(db.Integer, primary_key=True)

    sku = db.Column(
        db.String(50),
        nullable=False
    )

    location = db.Column(
        db.String(50)
    )

    transaction_type = db.Column(
        db.String(50)
    )

    quantity = db.Column(
        db.Integer
    )

    note = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
