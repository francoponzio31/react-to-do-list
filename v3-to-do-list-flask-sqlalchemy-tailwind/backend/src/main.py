from flask import Flask, render_template
from blueprints.tasks_bp import tasks_bp
from flask_cors import CORS
import os
from db.db_connection import db


static_folder_path = os.getenv("STATIC_FOLDER_PATH") or "../../frontend/dist"

app = Flask(
    __name__,
    static_url_path="",
    static_folder=static_folder_path,
    template_folder=static_folder_path
)

# DB connection
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rootpassword@db/to_do_list"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Blueprints:
app.register_blueprint(tasks_bp)

# CORS
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:8000"]}})

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)