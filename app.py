from flask import Flask, render_template
from config import Config
from extensions import db

from routes.upload import upload_bp
from routes.orders import orders_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(upload_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)