"""Database access: one SQLite connection per request, plus CLI commands.

Use get_db() inside a request or app context to get the connection.
Rows behave like dicts: row["title"].
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from .errors import LibraryError

# Fake sample data only (title, author, copies).
SAMPLE_BOOKS = [
    ("1984", "George Orwell", 3),
    ("Brave New World", "Aldous Huxley", 2),
    ("Clean Code", "Robert C. Martin", 2),
    ("Crime and Punishment", "Fyodor Dostoevsky", 1),
    ("Dune", "Frank Herbert", 2),
    ("Pride and Prejudice", "Jane Austen", 3),
    ("The Hobbit", "J.R.R. Tolkien", 2),
    ("The Little Prince", "Antoine de Saint-Exupery", 4),
    ("The Pragmatic Programmer", "Andrew Hunt and David Thomas", 1),
    ("To Kill a Mockingbird", "Harper Lee", 2),
]

SAMPLE_MEMBERS = [
    ("Jane Doe", "jane.doe@example.com"),
    ("John Smith", "john.smith@example.com"),
    ("Alex Kowalski", "alex.kowalski@example.com"),
]


def get_db():
    """Return the connection for the current request, opening it if needed."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Delete all data and create empty tables from schema.sql."""
    db = get_db()
    with current_app.open_resource("schema.sql") as schema:
        db.executescript(schema.read().decode("utf8"))


def seed_db(db):
    """Insert the sample books and members into an empty database."""
    if db.execute("SELECT COUNT(*) FROM book").fetchone()[0] > 0:
        raise LibraryError(
            "The database already has data. Run 'flask init-db' first."
        )
    db.executemany(
        "INSERT INTO book (title, author, total_copies, available_copies)"
        " VALUES (?, ?, ?, ?)",
        [(title, author, copies, copies) for title, author, copies in SAMPLE_BOOKS],
    )
    db.executemany(
        "INSERT INTO member (name, email) VALUES (?, ?)", SAMPLE_MEMBERS
    )
    db.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Create empty tables (deletes existing data)."""
    init_db()
    click.echo("Initialized the database.")


@click.command("seed")
@with_appcontext
def seed_command():
    """Add sample books and members."""
    try:
        seed_db(get_db())
    except LibraryError as error:
        click.echo(str(error))
        return
    click.echo(
        f"Added {len(SAMPLE_BOOKS)} books and {len(SAMPLE_MEMBERS)} members."
    )


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_command)
