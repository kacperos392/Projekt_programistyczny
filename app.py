from flask import Flask
from config import Config
from database import init_db
from routes.cars import cars_bp
from routes.analysis import analysis_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app.config["DATABASE"])

    app.register_blueprint(cars_bp)
    app.register_blueprint(analysis_bp)

    @app.get("/")
    def home():
        from flask import redirect, url_for
        return redirect(url_for("cars.list_cars"))

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
