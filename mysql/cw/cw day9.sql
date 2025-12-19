SELECT book_id, title, name
FROM books
LEFT JOIN borrowers
ON books.book_id = borrowers.book_id;

SELECT borrower_id, name, book_id, title
FROM borrowers
LEFT JOIN books
ON borrowers.book_id = books.book_id;

SELECT book_id, title
FROM books
LEFT JOIN borrowers
ON books.book_id = borrowers.book_id
WHERE borrowers.book_id IS NULL;

SELECT borrower_id, name, title
FROM borrowers
LEFT JOIN books
ON borrowers.book_id = books.book_id;
