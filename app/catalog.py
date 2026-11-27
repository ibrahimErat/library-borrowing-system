def list_books(db):
    """Return all books ordered by title."""
    rows = db.execute(
        "SELECT id, title, author, total_copies, available_copies "
        "FROM book ORDER BY title"
    ).fetchall()
    return [dict(row) for row in rows]

def get_book(db, book_id):
    """Return one book by its ID, or None."""
    row = db.execute(
        "SELECT id, title, author, total_copies, available_copies "
        "FROM book WHERE id = ?",
        (book_id,)
    ).fetchone()
    return dict(row) if row is not None else None