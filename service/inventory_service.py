"""Inventory service blueprint.

This module provides a Flask blueprint to render and handle the cycle count
form. The HTML template lives at templates/cycle_count.html.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/cycle-count', methods=('GET', 'POST'))
def cycle_count():
    """Render and handle the cycle count form.

    POST behavior:
      - validate sku and location
      - convert expected/count quantities to integers
      - log the submission (TODO: persist to DB or call a service layer)
      - flash a message and redirect back to the form
    """
    if request.method == 'POST':
        sku = (request.form.get('sku') or '').strip()
        location = (request.form.get('location') or '').strip()
        expected_qty_raw = request.form.get('expected_qty')
        counted_qty_raw = request.form.get('counted_qty')

        if not sku or not location:
            flash('SKU and Location are required.', 'danger')
            return redirect(url_for('inventory.cycle_count'))

        try:
            expected_qty = int(expected_qty_raw) if expected_qty_raw is not None else 0
            counted_qty = int(counted_qty_raw) if counted_qty_raw is not None else 0
        except (TypeError, ValueError):
            flash('Expected and Counted quantities must be integers.', 'danger')
            return redirect(url_for('inventory.cycle_count'))

        # TODO: persist this record to your DB or service layer
        current_app.logger.info(
            'Inventory count submitted: sku=%s location=%s expected=%d counted=%d',
            sku, location, expected_qty, counted_qty,
        )

        flash('Inventory count submitted successfully.', 'success')
        return redirect(url_for('inventory.cycle_count'))

    return render_template('cycle_count.html')
