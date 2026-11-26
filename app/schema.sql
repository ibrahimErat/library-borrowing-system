-- Library Borrowing System database schema.
-- "flask init-db" runs this file: it deletes all data and creates empty tables.

DROP TABLE IF EXISTS loan;
DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS book;

CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  total_copies INTEGER NOT NULL CHECK (total_copies >= 1),
  available_copies INTEGER NOT NULL
);

CREATE TABLE member (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

CREATE TABLE loan (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  member_id INTEGER NOT NULL REFERENCES member(id),
  book_id INTEGER NOT NULL REFERENCES book(id),
  borrow_date TEXT NOT NULL,   -- ISO date "YYYY-MM-DD"
  due_date TEXT NOT NULL,      -- ISO date "YYYY-MM-DD"
  return_date TEXT             -- NULL while the loan is active
);
