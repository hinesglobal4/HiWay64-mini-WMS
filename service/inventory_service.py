{% extends "base.html" %}

{% block content %}

<div class="container mt-4">

    <h1>Cycle Count</h1>

    <div class="card">

        <div class="card-header">
            Submit Inventory Count
        </div>

        <div class="card-body">

            <form method="POST">

                <div class="mb-3">

                    <label class="form-label">
                        SKU
                    </label>

                    <input
                        type="text"
                        name="sku"
                        class="form-control"
                        required>

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Location
                    </label>

                    <input
                        type="text"
                        name="location"
                        class="form-control"
                        required>

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Expected Quantity
                    </label>

                    <input
                        type="number"
                        name="expected_qty"
                        class="form-control"
                        required>

                </div>

                <div class="mb-3">

                    <label class="form-label">
                        Counted Quantity
                    </label>

                    <input
                        type="number"
                        name="counted_qty"
                        class="form-control"
                        required>

                </div>

                <button
                    class="btn btn-primary">

                    Submit Count

                </button>

            </form>

        </div>

    </div>

</div>

{% endblock %}
