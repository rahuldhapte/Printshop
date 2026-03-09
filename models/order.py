from datetime import datetime
from extensions import db

class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    pages = db.Column(db.Integer)
    copies = db.Column(db.Integer)
    print_type = db.Column(db.String(20))
    price = db.Column(db.Integer)
    status = db.Column(db.String(50), default="uploaded")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)