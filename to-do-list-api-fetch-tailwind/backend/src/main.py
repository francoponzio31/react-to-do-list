from flask import Flask, render_template
from blueprints.tasks_bp import tasks_bp
from flask_cors import CORS
import os

static_folder_path = os.getenv("STATIC_FOLDER_PATH") or "../../frontend/dist"

app = Flask(
    __name__,
    static_url_path="",
    static_folder=static_folder_path,
    template_folder=static_folder_path
)

CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:8000"]}})
app.register_blueprint(tasks_bp)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)