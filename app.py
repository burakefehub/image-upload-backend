from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Backend is running 🚀"

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No image sent"}), 400

    file = request.files["image"]
    filename = file.filename

    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    img = Image.open(path)
    width, height = img.size

    return jsonify({
        "message": "Image uploaded successfully",
        "filename": filename,
        "width": width,
        "height": height
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
