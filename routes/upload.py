import os
from flask import Blueprint, request, jsonify, current_app
from services.page_counter import count_pages
from flask import render_template

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    pages = count_pages(filepath)

    return render_template(
        "print_options.html",
        filename = file.filename,
        pages = pages
    )