from flask import Flask


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(DATABASE="library.db")
    if config:
        app.config.update(config)

    @app.get("/")
    def index():
        return (
            "<h1>Library Borrowing System</h1>"
            "<p>Sprint 0 skeleton is running.</p>"
        )

    @app.get("/health")
    def health():
        return {"status": "ok"}

    from app.routes.books import bp as books_bp
    app.register_blueprint(books_bp)

    return app