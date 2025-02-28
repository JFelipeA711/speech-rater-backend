from flask import Flask, request, jsonify # type: ignore
import os
from werkzeug.utils import secure_filename # type: ignore

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/evaluate_audio", methods=["POST"])
def evaluate_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    
    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    
    # Aquí iría la lógica para analizar el audio y calcular el puntaje
    # Por ahora, simularemos un puntaje aleatorio
    import random
    score = round(random.uniform(0, 120), 2)
    
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
