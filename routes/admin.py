from flask import Blueprint, render_template
from models.order import Order

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin_dashboard():

    orders = Order.query.order_by(Order.created_at.desc()).all()

    return render_template("admin.html", orders=orders)