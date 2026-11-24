# Product Backlog

The live backlog is the GitHub board: https://github.com/ibrahimErat/library-borrowing-system/projects. This file is the Sprint 0 starting version used to create the issues. Every story becomes one issue with the label `user-story` and its priority.

**Order rationale:** books must exist before they can be borrowed, and members must exist before loans, so book management comes first (dependency). Borrowing and returning are the core value of the product, so they follow immediately. Search, overdue tracking and history add value on top of the core and come last. Login is a stretch goal because it adds risk without being needed to demonstrate the main journeys.

## User journeys

- **J1 – Borrow a book:** a student opens the book list, finds a book, sees that a copy is available and borrows it. The due date is shown.
- **J2 – Return a book:** a student returns a borrowed book and sees it in their borrowing history with the return date.
- **J3 – Manage the library:** a librarian adds new books, corrects book details and checks which loans are overdue.

## Stories

| ID | Story | Priority | Sprint | Req. |
|---|---|---|---|---|
| US-01 | Add a book | Must | 1 | FR06 |
| US-02 | List books with availability | Must | 1 | FR02, FR06 |
| US-03 | Edit a book | Must | 1 | FR06 |
| US-04 | Delete a book | Should | 1 | FR06 |
| US-05 | Register a member | Must | 2 | FR07 |
| US-06 | Borrow a book | Must | 2 | FR03, FR08 |
| US-07 | Return a book | Must | 2 | FR04, FR08 |
| US-08 | Search books by title or author | Should | 3 | FR01 |
| US-09 | See overdue loans | Should | 3 | FR09 |
| US-10 | See my borrowing history | Should | 3 | FR05 |
| US-11 | Log in with a role | Could | stretch | — |

### Story split example

The original requirement **FR06 "Manage books"** was too large for one issue. It was split into four independently demonstrable stories: **US-01 add**, **US-02 list**, **US-03 edit** and **US-04 delete**. Each can be built, tested and shown on its own.

---

### US-01 Add a book
*As a librarian, I want to add a new book so that students can find and borrow it.*

- Given the add-book form, when I enter a title, author and number of copies (≥ 1) and save, then the book appears in the book list.
- Available copies are set equal to total copies for a new book.
- Title and author are required; an empty field shows an error and nothing is saved.
- Number of copies must be a whole number ≥ 1.

### US-02 List books with availability
*As a student, I want to see all books with the number of available copies so that I know what I can borrow.*

- The list shows title, author, total copies and available copies.
- Books with 0 available copies are clearly marked "Not available".
- If there are no books, the page shows "No books yet".

### US-03 Edit a book
*As a librarian, I want to correct a book's details so that the catalogue stays accurate.*

- I can change title, author and total copies.
- Total copies cannot be set lower than the number of copies currently on loan.
- After saving, the list shows the new values.

### US-04 Delete a book
*As a librarian, I want to remove a book that the library no longer has so that students do not try to borrow it.*

- A book with no active loans can be deleted and disappears from the list.
- A book with active loans cannot be deleted; an error explains why.

### US-05 Register a member
*As a librarian, I want to register a student as a member so that they can borrow books.*

- Name and email are required; email must be unique.
- After registration the member appears in the member list.

### US-06 Borrow a book
*As a student, I want to borrow a book so that I can read it at home.*

- The book must have at least one available copy (BR01).
- The member must have fewer than three active loans (BR02).
- The system records the borrow date and sets the due date to 14 days later (BR03).
- Available copies decrease by one (BR05).
- If a rule is broken, the loan is not created and the reason is shown.

### US-07 Return a book
*As a student, I want to return a borrowed book so that others can borrow it.*

- The loan gets a return date and is no longer active.
- Available copies increase by one (BR06).
- A loan that is already returned cannot be returned again.

### US-08 Search books by title or author
*As a student, I want to search by title or author so that I can find a book quickly.*

- Search is case-insensitive and matches part of the title or author.
- An empty result shows "No books found".

### US-09 See overdue loans
*As a librarian, I want to see overdue loans so that I can contact the members.*

- A loan is overdue when today is after the due date and it is not returned (BR04).
- The list shows member, book, due date and days overdue.

### US-10 See my borrowing history
*As a student, I want to see my borrowing history so that I know what I have borrowed and when to return it.*

- Shows each loan with borrow date, due date and return date (or "Not returned").
- Active loans are shown first.

### US-11 Log in with a role (stretch)
*As a user, I want to log in as a student or librarian so that I only see the actions for my role.*

- Only implemented if Sprint 3 has spare capacity.

## Business rules

| ID | Rule |
|---|---|
| BR01 | A book cannot be borrowed when no copies are available. |
| BR02 | A member can have at most three active loans at a time. |
| BR03 | The loan period is 14 days. |
| BR04 | A loan is overdue when the due date has passed and the book has not been returned. |
| BR05 | Borrowing a book decreases its available copies by one. |
| BR06 | Returning a book increases its available copies by one. |

## Quality scenarios (non-functional requirements)

| ID | Quality | Scenario | Measure | How we check it |
|---|---|---|---|---|
| QS-01 | Data integrity | A student tries to borrow a book with 0 available copies, or returns a book twice. | Available copies are always between 0 and total copies; the invalid action is rejected. | Automated unit tests for BR01, BR05, BR06 |
| QS-02 | Performance | A student searches the catalogue that contains 1,000 books. | Results are returned in under 1 second on a normal laptop. | Automated test with 1,000 seeded books and a time limit |
| QS-03 | Usability | A student who has never used the app wants to borrow a book. | Borrowing takes at most 3 clicks from the book list. | Manual check during the sprint review |
| QS-04 | Maintainability | A new team member sets up the project. | The app runs from the README instructions in under 10 minutes; CI runs all tests on every pull request. | Smoke test on another member's machine; CI run history |

## Technical tasks (Sprint 0)

| ID | Task |
|---|---|
| TS-01 | Create repository, board and README |
| TS-02 | Flask skeleton that runs locally |
| TS-03 | First automated test merged through a reviewed pull request |
| TS-04 | GitHub Actions CI running the tests on pull requests |
