import os

from flask import Flask, redirect


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        DATABASE=os.path.join(app.instance_path, "library.db"),
    )
    if config:
        app.config.update(config)
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    # Register blueprints here, e.g.:
    # from .routes import books
    # app.register_blueprint(books.bp)

    @app.get("/")
    def index():
        return redirect("/books")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
