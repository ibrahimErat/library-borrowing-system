# Architecture

## Sprint 0 sketch

A simple three-part web application. The diagrams render automatically on GitHub.

```mermaid
flowchart LR
    U["Student / Librarian<br/>(web browser)"] -->|HTTP requests,<br/>HTML forms| F
    subgraph F["Flask application (Python)"]
        R["Routes<br/>(pages and forms)"] --> S["Domain logic<br/>(books, members, loans,<br/>business rules BR01–BR06)"]
        S --> D["Data access"]
    end
    D -->|SQL| DB[("SQLite database<br/>Book · Member · Loan")]
    T["pytest + GitHub Actions CI"] -.->|tests every pull request| F
```

- **Frontend:** HTML pages rendered by Flask templates, with CSS and a little JavaScript.
- **Backend:** Flask routes call the domain logic. Business rules live in the domain logic, not in the routes, so they can be unit-tested without a browser.
- **Database:** SQLite file. Each table has a unique ID.
- **Quality:** pytest for unit and route tests; GitHub Actions runs them on every pull request.

No REST API, microservices or extra patterns are planned: the product is a single small web app and does not need them.

## Use-case view

```mermaid
flowchart LR
    Student((Student))
    Librarian((Librarian))
    Student --- UC1[Search books]
    Student --- UC2[Check availability]
    Student --- UC3[Borrow a book]
    Student --- UC4[Return a book]
    Student --- UC5[View borrowing history]
    Librarian --- UC6[Manage books]
    Librarian --- UC7[Register members]
    Librarian --- UC8[View overdue loans]
```

## Initial domain model

```mermaid
classDiagram
    class Book {
        id
        title
        author
        total_copies
        available_copies
    }
    class Member {
        id
        name
        email
    }
    class Loan {
        id
        borrow_date
        due_date
        return_date
        is_active()
        is_overdue(today)
    }
    Member "1" --> "0..*" Loan : has
    Book "1" --> "0..*" Loan : is borrowed in
```

## Architecture decision records

### ADR-001: Flask + SQLite monolith (Sprint 0)

- **Context:** small team, short timeline, some members are new to web development.
- **Options:** (a) Flask + SQLite single app; (b) separate frontend framework (React) + REST API backend.
- **Decision:** (a) Flask + SQLite.
- **Consequences:** + one language (Python), fast setup, no server needed for the database, easy to test with pytest. − Less suitable for many simultaneous users; acceptable for the semester scope.

*(Sprint 2 adds an ADR based on a quality scenario.)*
