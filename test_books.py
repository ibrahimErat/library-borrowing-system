
from app import create_app

def test_books_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200
    assert b"Books" in response.data
    assert b"No books yet" in response.data
