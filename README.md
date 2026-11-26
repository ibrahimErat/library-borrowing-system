# Library Borrowing System

A small web application where students can find, borrow and return library books, and librarians can manage the book collection and monitor loans.

Semester project for **Software Development Methodologies 2026/2027** (Scrum + XP).

## Team

| Member | GitHub |
|---|---|
| İbrahim Erat | `<username>` |
| Abubakr Gafarov | `<username>` |
| Mert Gumus | `<username>` |
| Dinkinesh Nure | `<username>` |
| Yiğidhan Soytürk | `<username>` |

## Links

- Issue board: `<GitHub Projects link>`
- Living project report: [docs/report.md](docs/report.md)
- Team agreement and Definition of Done: [docs/team-agreement.md](docs/team-agreement.md)
- Sprint records: [docs/sprints/](docs/sprints/)

## Tech stack

Python 3.9+ · Flask · SQLite · pytest · GitHub Actions

## Run locally

```bash
git clone <repository-url>
cd library-borrowing-system
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app init-db          # create empty tables (deletes existing data)
flask --app app seed             # add 10 sample books and 3 sample members
flask --app app run
```

Open http://127.0.0.1:5000 in a browser. The health check is at http://127.0.0.1:5000/health.
The database file is `instance/library.db` (not committed to Git).

## Building a feature on the database

- **Connection:** `from app.db import get_db` → `db = get_db()` inside a route. Rows work like dicts: `book["title"]`. Call `db.commit()` after writing.
- **Rule broken?** `from app.errors import LibraryError` → `raise LibraryError("Readable message")`. The route catches it and calls `flash(str(error), "error")`.
- **Pages:** start each template with `{% extends "base.html" %}` and put the page inside `{% block content %}`. The layout already has the navigation and shows flashed messages.
- **Routes:** add them to a Blueprint in `app/routes/` (for example `books.py` with `bp = Blueprint("books", __name__)`) and register it in `create_app()` in `app/__init__.py`.
- **Tests:** use the `db` fixture to test functions directly and the `client` fixture to test pages. Each test gets a new, empty database.

```python
def test_add_book_sets_available_copies(db):
    book_id = add_book(db, "Dune", "Frank Herbert", 2)
    book = get_book(db, book_id)
    assert book["available_copies"] == 2
```

## Run the tests

```bash
pytest -v
```

The same tests run automatically on every pull request and on every push to `main` (see [.github/workflows/ci.yml](.github/workflows/ci.yml)).

## How we work

1. Pick an issue from the board and move it to **In Progress**.
2. Create a branch: `feature/<issue-number>-short-name` (e.g. `feature/12-add-book`).
3. Commit, push and open a pull request that says `Closes #<issue-number>`.
4. Another team member reviews it. CI must be green.
5. Merge to `main`; the issue moves to **Done**.

Full rules: [docs/team-agreement.md](docs/team-agreement.md).
