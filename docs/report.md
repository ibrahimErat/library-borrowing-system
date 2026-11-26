# Library Borrowing System

## Project Report

**Course:** Software Development Methodologies 2026/2027  
**Project:** Library Borrowing System  
**Repository:** `ibrahimErat/library-borrowing-system`  
**Last updated:** 19 November 2026

## A. General Information

| Item | Description |
|---|---|
| Project title | Library Borrowing System |
| Course | Software Development Methodologies 2026/2027 |
| Team members | İbrahim Erat, Abubakr Gafarov, Mert Gumus, Dinkinesh Nure, Yiğidhan Soytürk |
| Programming language | Python |
| Backend | Flask |
| Database | SQLite |
| Version control | GitHub |
| Final version | To be completed in Sprint 3 |

## B. Problem and Scope

### Problem

Small libraries often manage books and borrowing records using paper or spreadsheets. Students cannot easily check book availability, and librarians may have difficulty tracking borrowed books and overdue returns.

### Product Goal

Our goal is to develop a simple web application that allows students to search for books, check availability, borrow and return books, and view their borrowing history.

Librarians will be able to manage books, register members, and monitor overdue loans.

### Target Users

**Students (Members)**

- Search for books.
- Check book availability.
- Borrow and return books.
- View borrowing history.

**Librarians**

- Add, edit, and delete books.
- Register members.
- Manage library records.
- View overdue loans.

### Intended Value

Students can easily find available books, while librarians can manage books and borrowing records in one system.

### User Journeys

1. Borrow a book.
2. Return a book.
3. Manage the library.

### Assumptions

- The system is designed for one library location.
- Librarians register students as members.
- Students select their member account when using the system.
- Sample data will be used for testing.

### Out of Scope

- Online payments and late fees.
- Email and SMS notifications.
- Mobile applications.
- Book reservations.
- Multiple library branches.
- External catalogue integration.

## C. Requirements

### Functional Requirements

The system includes the following main requirements:

| ID | Requirement |
|---|---|
| FR01 | Search books by title or author. |
| FR02 | Check book availability. |
| FR03 | Borrow books. |
| FR04 | Return books. |
| FR05 | View borrowing history. |
| FR06 | Manage books. |
| FR07 | Register members. |
| FR08 | Manage borrowing records. |
| FR09 | Monitor overdue loans. |

Detailed user stories and acceptance criteria are documented in `docs/backlog.md`.

### Business Rules

| ID | Business Rule |
|---|---|
| BR01 | A book cannot be borrowed when no copies are available. |
| BR02 | A member can borrow a maximum of three books at a time. |
| BR03 | The borrowing period is 14 days. |
| BR04 | A loan is overdue when its due date has passed and it has not been returned. |
| BR05 | Borrowing a book decreases its available copies by one. |
| BR06 | Returning increases its available copies by one. |

### Quality Requirements

| ID | Quality | Requirement |
|---|---|---|
| QS-01 | Data Integrity | Available copies must remain between zero and total copies. |
| QS-02 | Performance | Searching 1,000 books should take less than one second. |
| QS-03 | Usability | Borrowing should take no more than three clicks from the book list. |
| QS-04 | Maintainability | A new team member should be able to run the application using the README instructions in under ten minutes. |

### Requirement Changes

| Date | Change | Reason |
|---|---|---|
| 17 November 2026 | Login moved to a stretch goal. | Reduce development risk and focus on the main features. |
| 7 November 2026 | Book management divided into smaller user stories. | Make development and testing easier. |
| 7 November 2026 | Students handle borrowing and returning. | Give each user role clear responsibilities. |

## D. Domain and Design

The system has three main domain entities:

**Book:** Stores book information, including title, author, total copies, and available copies.

**Member:** Stores registered student information, including name and email.

**Loan:** Records borrowing information, including borrow date, due date, and return date.

### System Architecture

The application uses a simple three-part architecture:

1. Frontend: HTML templates, CSS, and JavaScript.
2. Backend: Python Flask.
3. Database: SQLite.

Flask routes communicate with the domain logic, which handles business rules and database operations.

Automated tests are written using pytest, and GitHub Actions runs tests automatically.

Detailed architecture diagrams and technical decisions are documented in `docs/architecture.md`.

The project also uses the concepts of Catalog and Lending to separate book management from borrowing operations.

## E. Development Process

### Methodology: Scrum with XP Practices

Our team uses Scrum with selected Extreme Programming (XP) practices.

**Scrum**

Scrum helps our team organize work into short sprints, set goals, review progress, and improve collaboration.

**XP Practices**

We use:

- Test-first development.
- Pair programming.
- Code reviews.
- Small pull requests.
- Continuous Integration.

These practices help improve code quality and make teamwork easier.

### Development Timeline

| Sprint | Dates | Main Goal |
|---|---|---|
| Sprint 0 | 17–23 November 2026 | Setup and project planning |
| Sprint 1 | 24–30 November 2026 | Book management |
| Sprint 2 | 1–13 December 2026 | Members, borrowing, and returning |
| Sprint 3 | 14 December 2026–10 January 2027 | Search, overdue loans, history, and testing |
| Final | From 11 January 2027 | Final demonstration and individual defense |

### Sprint 0

Sprint 0 focuses on project setup, requirements, architecture, backlog preparation, team agreement, and GitHub collaboration.

The Sprint 0 review and retrospective will be documented in `docs/sprints/sprint-0.md`.

### Future Sprints

Sprint 1: Book management.

Sprint 2: Member registration, borrowing, and returning.

Sprint 3: Book searching, overdue tracking, borrowing history, testing, and final improvements.

## F. Implementation and Quality

### Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend framework |
| SQLite | Database |
| HTML | Website structure |
| CSS | Website styling |
| JavaScript | Basic website interactions |
| pytest | Automated testing |
| GitHub Actions | Continuous Integration |

### Development Approach

The team follows a modular development approach.

Book management is handled separately from borrowing operations to keep the system organized and easier to maintain.

### Testing Strategy

We will use automated unit tests to check business rules and route tests to check website functionality.

GitHub Actions will automatically execute tests when code is pushed or a pull request is created.

### CI/CD

The project uses GitHub Actions for Continuous Integration.

The workflow automatically installs dependencies and runs automated tests.

Additional testing results and implementation evidence will be added during future sprints.

## G. Evaluation

This section will be completed in Sprint 3.

It will evaluate:

- Whether the project meets its requirements.
- Whether the main user journeys work correctly.
- Testing results.
- Scrum and XP practices.
- Project limitations.
- Possible future improvements.

## H. Individual Contributions

| Team Member | Sprint 0 Responsibilities |
|---|---|
| İbrahim Erat | Repository, website skeleton, automated tests, and CI. |
| Abubakr Gafarov | Product backlog and user story issues. |
| Mert Gumus | Team agreement and Definition of Done. |
| Dinkinesh Nure | Project definition, requirements draft, scope, and user journeys. |
| Yiğidhan Soytürk | Glossary, risks, and architecture documentation. |

Each member's contributions will be updated with GitHub issue, pull request, and review links throughout the semester.

## I. References and Reproduction

### Project Resources

- GitHub repository: https://github.com/ibrahimErat/library-borrowing-system
- Project board: https://github.com/users/ibrahimErat/projects/1
- Setup instructions: `README.md`
- Product backlog: `docs/backlog.md`
- Architecture: `docs/architecture.md`
- Team agreement: `docs/team-agreement.md`
- Glossary: `docs/glossary.md`
- Risk list: `docs/risks.md`

### References

- Agile Manifesto.
- The Scrum Guide.
- Atlassian Agile Coach.

### Reproduction

The application can be installed and executed using the setup instructions in the project README.

Testing instructions and database initialization steps will also be documented there.

---

**Document Status:** Sprint 0 Draft  
**Prepared by:** Dinkinesh Nure  
**Reviewer:** Yiğidhan Soytürk
