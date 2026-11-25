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


    
    @app.get("/books")
    def list_books():
        books = []
        if not books:
            return "<h1>Books</h1><p>No books yet</p>"

    return app
