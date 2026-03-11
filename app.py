from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

# folder upload
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# buat folder jika belum ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# simpan statistik sederhana
stats = {
    "Healthy": 0,
    "Blight": 0,
    "Rust": 0
}

# homepage sistem informasi
@app.route("/")
def home():
    return render_template("home.html")
# dashboard statistik
@app.route("/dashboard")
def index():
    return render_template("index.html", stats=stats)

# halaman upload
@app.route("/upload")
def upload():
    return render_template("upload.html")

# halaman dataset
@app.route("/dataset")
def dataset():
    return render_template("dataset.html")


# halaman accuracy
@app.route("/accuracy")
def accuracy():
    return render_template("result.html")

# route prediksi
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # simulasi prediksi
    prediction = random.choice(["Healthy", "Blight", "Rust"])

    # update statistik
    stats[prediction] += 1

    return render_template(
        "result.html",
        prediction=prediction,
        image_path=filepath
    )

if __name__ == "__main__":
    app.run(debug=True)
    

    