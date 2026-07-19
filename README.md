# HiWay64 Mini-WMS

HiWay64 Mini-WMS is a Python-based Warehouse Management System built with Flask and SQLAlchemy.

## Business Problem

Many warehouse management systems focus only on storing inventory transactions.
Real distribution centers must also enforce operational constraints such as:

- Hazardous material segregation
- Temperature-controlled storage
- Product family restrictions
- Space utilization
- Inventory accuracy monitoring

This project was built to simulate how a WMS can use business rules to reduce operational risk and improve inventory placement decisions.
The goal is to demonstrate both technical development skills and supply-chain domain expertise through a realistic warehouse management platform.

Features include:

- Inventory Management
- Receiving Operations
- Warehouse Locations
- Cycle Counting
- Inventory Accuracy KPIs
- Operational Dashboards
- Rule-Based Location Validation
- Hazardous Material Segregation
- Temperature Zone Enforcement
- Dynamic Slotting Optimization
- Put-away Recommendations
- Transaction Audit Logging


## Architecture

The application follows an optimal three-layer architecture:

Presentation Layer
- HTML
- Bootstrap
- Jinja Templates

Business Logic Layer
- Inventory Services
- Receiving Services
- KPI Services
- Validation Services
- Slotting Services
- Cycle Count Services

Data Layer
- SQLAlchemy Models
- SQLite Database


## Rule-Based Location Intelligence

The WMS includes a validation engine that evaluates inventory placement before assignment.

Current validations:

- Hazardous material segregation
- Temperature zone enforcement
- Product family restrictions
- Slotting recommendations

Example:

A flammable product cannot be assigned near oxidizer inventory.

Frozen inventory cannot be assigned to ambient storage locations.


## Transportation and LTL Concepts

Products may store:

- Freight Class
- NMFC Codes (National Motor Freight Classification)
- Product Family
- Hazard Classification

This functionality reflects real-world LTL and distribution operations.


## Planned Enhancements

- REST API implementation
- Role-based security
- Barcode scanning integration
- PostgreSQL migration
- Automated replenishment logic
- Pick path optimization
- Docker deployment
- AWS cloud deployment

// Future requirements additions //
Flask-Migrate
Flask-Login
psycopg2-binary
pytest

