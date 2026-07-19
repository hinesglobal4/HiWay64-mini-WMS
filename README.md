# HiWay64 Mini-WMS

HiWay64 Mini-WMS is a Python-based Warehouse Management System built with Flask and SQLAlchemy.

The platform combines software engineering principles with real-world warehouse, distribution, and LTL transportation concepts.
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

The project models operational controls commonly found in warehouse and logistics environments, emphasizing inventory accuracy, location intelligence, storage compliance, and warehouse efficiency.


## Architecture

The application follows a three-layer architecture:

Presentation Layer
- HTML
- Bootstrap
- Jinja Templates

Business Logic Layer
- Inventory Services
- Receiving Services
- KPI Services
- Validation Services

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
