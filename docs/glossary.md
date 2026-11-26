# Glossary

The team uses these words with exactly these meanings in stories, code and tests. The glossary is extended in Sprint 2.

| Term | Meaning | In code |
|---|---|---|
| **Book** | A title in the library catalogue (title + author). One book can have several physical copies. | `Book` |
| **Total copies** | How many physical copies of a book the library owns. | `total_copies` |
| **Available copies** | Copies that are currently not on loan and can be borrowed. Always between 0 and total copies. | `available_copies` |
| **Member** | A student registered by a librarian who is allowed to borrow books. | `Member` |
| **Librarian** | Staff user who manages books and members and monitors loans. | — |
| **Loan** | The record that one member borrowed one copy of one book. | `Loan` |
| **Active loan** | A loan that has not been returned yet (no return date). | `is_active` |
| **Borrow** | Creating a new loan for a member and a book. | `borrow()` |
| **Return** | Closing an active loan by setting its return date. | `return_book()` |
| **Borrow date** | The day the loan was created. | `borrow_date` |
| **Due date** | The day the book must be returned: borrow date + 14 days. | `due_date` |
| **Return date** | The day the book was returned. Empty for active loans. | `return_date` |
| **Overdue** | An active loan whose due date is before today. | `is_overdue` |
| **Borrowing history** | All loans of one member, active and returned. | — |
