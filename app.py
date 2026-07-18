from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from data.models import db

from service.inventory_service import InventoryService

from service.cycle_count_service import CycleCountService

from service.kpi_service import KPIService


from flask import Flask

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

@app.route("/")
def home():
    return "Mini WMS Running"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/dashboard")
def dashboard():

    metrics = {
        "inventory_accuracy": 98.3,
        "inventory_units": 12450,
        "receipts": 23,
        "variances": 4
    }

    alerts = [
        "Aisle B temperature warning",
        "2 inventory variances require review",
        "No hazardous material conflicts detected"
    ]

    recent_activity = [
        "Received SKU CHEM001",
        "Cycle count completed at A-01-01",
        "Transferred inventory to B-03-02"
    ]

    return render_template(
        "dashboard.html",
        metrics=metrics,
        alerts=alerts,
        recent_activity=recent_activity
    )
