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
flask --app app run
```

Open http://127.0.0.1:5000 in a browser. The health check is at http://127.0.0.1:5000/health.

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
