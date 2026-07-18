from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sku = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    weight = db.Column(
        db.Float
    )

    freight_class = db.Column(
        db.String(20)
    )

    product_family = db.Column(
        db.String(50)
    )

    hazard_class = db.Column(
        db.String(50)
    )   

class Location(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    code = db.Column(
        db.String(50),
        unique=True
    )

    zone = db.Column(
        db.String(50)
    )

class Inventory(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sku = db.Column(
        db.String(50)
    )

    location = db.Column(
        db.String(50)
    )

    quantity = db.Column(
        db.Integer,
        default=0
    )

class WarehouseRule(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    primary_family = db.Column(
        db.String(50)
    )

    restricted_family = db.Column(
        db.String(50)
    )

    minimum_aisles = db.Column(
        db.Integer
    )

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
