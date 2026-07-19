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

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

@app.route("/")
def home():

    return redirect(
        url_for("dashboard")
    )

@app.route("/dashboard")
def dashboard():

    metrics = {
        "inventory_accuracy": 98.3,
        "inventory_units": 12450,
        "receipts": 23,
        "variances": 4,
        "warehouse_health": 96
    }

    alerts = [
        "Temperature zone warning in Cooler-02",
        "2 inventory variances require review",
        "Hazardous material validation passed",
        "No capacity issues detected"
    ]

    recent_activity = [
        "Received CHEM001 into HZ-01-05",
        "Cycle Count completed in A-01-01",
        "Inventory transfer completed to B-04-03"
    ]

    recommendations = [
        {
            "sku": "CHEM001",
            "recommended_location": "HZ-01-05",
            "reason": "Hazmat Zone"
        },
        {
            "sku": "SKU1001",
            "recommended_location": "A-01-01",
            "reason": "Fast Mover"
        }
    ]

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

    return render_template(
        "dashboard.html",
        metrics=metrics,
        alerts=alerts,
        recent_activity=recent_activity,
        recommendations=recommendations
    )
