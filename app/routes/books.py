from flask import Blueprint, render_template
from app.db import get_db
from app.catalog import list_books

bp = Blueprint("books", __name__)

@bp.get("/books")
def books_list():
    db = get_db()
    books = list_books(db)
    return render_template("books/list.html", books=books)