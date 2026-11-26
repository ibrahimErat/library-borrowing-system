import sqlite3

import pytest

from app.db import get_db, seed_db
from app.errors import LibraryError


def count(db, table):
    return db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]


def test_new_database_is_empty(db):
    assert count(db, "book") == 0
    assert count(db, "member") == 0
    assert count(db, "loan") == 0


def test_get_db_returns_the_same_connection_within_a_request(app):
    with app.app_context():
        assert get_db() is get_db()


def test_connection_is_closed_after_the_app_context(app):
    with app.app_context():
        db = get_db()

    with pytest.raises(sqlite3.ProgrammingError):
        db.execute("SELECT 1")


def test_rows_can_be_read_by_column_name(db):
    db.execute(
        "INSERT INTO book (title, author, total_copies, available_copies)"
        " VALUES ('Dune', 'Frank Herbert', 2, 2)"
    )
    book = db.execute("SELECT * FROM book").fetchone()

    assert book["title"] == "Dune"


def test_book_needs_at_least_one_copy(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO book (title, author, total_copies, available_copies)"
            " VALUES ('Dune', 'Frank Herbert', 0, 0)"
        )


def test_member_email_must_be_unique(db):
    db.execute("INSERT INTO member (name, email) VALUES ('Jane Doe', 'jane@example.com')")

    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO member (name, email) VALUES ('Jane Roe', 'jane@example.com')")


def test_loan_must_reference_an_existing_book_and_member(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO loan (member_id, book_id, borrow_date, due_date)"
            " VALUES (99, 99, '2026-11-26', '2026-12-10')"
        )


def test_seed_adds_sample_books_and_members(db):
    seed_db(db)

    assert count(db, "book") == 10
    assert count(db, "member") == 3
    assert count(db, "loan") == 0


def test_seeded_books_have_all_copies_available(db):
    seed_db(db)

    mismatched = db.execute(
        "SELECT COUNT(*) FROM book WHERE available_copies != total_copies"
    ).fetchone()[0]
    assert mismatched == 0


def test_seed_refuses_to_run_twice(db):
    seed_db(db)

    with pytest.raises(LibraryError):
        seed_db(db)


def test_init_db_command_creates_empty_tables(app):
    with app.app_context():
        seed_db(get_db())

    result = app.test_cli_runner().invoke(args=["init-db"])

    assert "Initialized" in result.output
    with app.app_context():
        assert count(get_db(), "book") == 0


def test_seed_command_adds_sample_data(app):
    result = app.test_cli_runner().invoke(args=["seed"])

    assert "Added 10 books and 3 members" in result.output


def test_seed_command_explains_when_data_exists(app):
    runner = app.test_cli_runner()
    runner.invoke(args=["seed"])

    result = runner.invoke(args=["seed"])

    assert "already" in result.output
