INSERT INTO books (id, title, genre) VALUES (1, 'Viy','horor')
INSERT INTO books (id, title, genre) VALUES (2, 'Chernovik','sci-fi')
INSERT INTO books (id, title, genre) VALUES (3, 'Chistovik','sci-fi')
INSERT INTO books (id, title, genre) VALUES (4, 'Razlom','sci-fi')
INSERT INTO books (id, title, genre) VALUES (5, 'Test book','test')
INSERT INTO authors (id, first_name, last_name) VALUES (1, 'Nikolay','Gogol')
INSERT INTO authors (id, first_name, last_name) VALUES (2, 'Sergey','Lukyanenko')
INSERT INTO authors (id, first_name, last_name) VALUES (3,'Sergey','Slyusarenko')
INSERT INTO authors (id, first_name, last_name) VALUES (4, 'Test','Author')
INSERT INTO books_authors (book_id, author_id) VALUES (1, 1)
INSERT INTO books_authors (book_id, author_id) VALUES (2, 2)
INSERT INTO books_authors (book_id, author_id) VALUES (3, 2)
INSERT INTO books_authors (book_id, author_id) VALUES (4, 2)
INSERT INTO books_authors (book_id, author_id) VALUES (4, 3)
INSERT INTO books_authors (book_id, author_id) VALUES (5, 4)
INSERT INTO users (id, login, password_hash, role) VALUES (0, 'admin', 'pbkdf2:sha256:50000$nPcmeBDi$82e6655256595857a2bc4826f2da6a47d66defcbf2341f1bd0e885ec795fadae', 1)
