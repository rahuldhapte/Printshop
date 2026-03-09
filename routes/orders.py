from flask import Blueprint, request, jsonify
from extensions import db
from models.order import Order

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/create-order", methods=["POST"])
def create_order():

    data = request.json

    order = Order(
        filename=data["filename"],
        pages=data["pages"],
        copies=data["copies"],
        print_type=data["print_type"],
        price=data["price"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({
        "message": "Order created successfully",
        "order_id": order.id
    })