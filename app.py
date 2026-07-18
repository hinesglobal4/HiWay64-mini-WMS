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

        "Location A-04-01 nearing capacity",

        "2 cycle count discrepancies",

        "No chemical conflicts detected"
    ]

    return render_template(
        "dashboard.html",
        metrics=metrics,
        alerts=alerts
    )
