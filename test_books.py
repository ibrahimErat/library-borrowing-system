
from app import create_app

def test_books_page():
    app = create_app()
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200
    assert b"Books" in response.data
    assert b"No books yet" in response.data


def test_books_page_shows_database_books(client, db):
    db.execute(
        "INSERT INTO book (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)",
        ("Dune", "Frank Herbert", 3, 2)
    )
    db.commit()

    response = client.get("/books")

    assert response.status_code == 200
    assert b"Dune" in response.data
    assert b"Frank Herbert" in response.data
    assert b"3" in response.data
    assert b"2" in response.data

def test_books_page_shows_not_available(client, db):
    db.execute(
        "INSERT INTO book (title, author, total_copies, available_copies) VALUES (?, ?, ?, ?)",
        ("Python Basics", "John Smith", 2, 0)
    )
    db.commit()

    response = client.get("/books")

    assert response.status_code == 200
    assert b"Python Basics" in response.data
    assert b"Not available" in response.data