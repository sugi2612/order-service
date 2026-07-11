from flask import Flask, jsonify, request

app = Flask(_name_)

# Sample Orders
orders = [
    {
        "id": 1,
        "user_id": 1,
        "product": "Laptop",
        "quantity": 1,
        "price": 70000
    },
    {
        "id": 2,
        "user_id": 2,
        "product": "Mobile",
        "quantity": 2,
        "price": 25000
    }
]

# Health Check
@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "Running"
    })

# Get all orders
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

# Get order by ID
@app.route("/orders/<int:id>", methods=["GET"])
def get_order(id):
    for order in orders:
        if order["id"] == id:
            return jsonify(order)
    return jsonify({"message": "Order not found"}), 404

# Create Order
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    order = {
        "id": len(orders) + 1,
        "user_id": data["user_id"],
        "product": data["product"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    orders.append(order)

    return jsonify(order), 201

# Update Order
@app.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):

    data = request.get_json()

    for order in orders:
        if order["id"] == id:
            order["product"] = data["product"]
            order["quantity"] = data["quantity"]
            order["price"] = data["price"]

            return jsonify(order)

    return jsonify({"message": "Order not found"}), 404

# Delete Order
@app.route("/orders/<int:id>", methods=["DELETE"])
def delete_order(id):

    for order in orders:
        if order["id"] == id:
            orders.remove(order)
            return jsonify({"message": "Order deleted"})

    return jsonify({"message": "Order not found"}), 404

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5001)
