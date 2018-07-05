# -*- coding: utf-8 -*-
from web import db
from .models import Book, Author
from .resources import Resources as Res


SEARCH_BY_TITLE = 'title'
SEARCH_BY_AUTHOR_LASTNAME = 'author'
SEARCH_ALL = 'all'


def search_book(search_text, criteria=SEARCH_BY_TITLE, serialize=False):
    processed_search_text = process_search_query(search_text)

    if criteria == SEARCH_BY_TITLE:
        raw_books = db.session.query(Book).filter(Book.title.ilike(processed_search_text))
    elif criteria == SEARCH_BY_AUTHOR_LASTNAME:
        raw_books = db.session.query(Book).join(Book.authors).filter(Author.last_name.ilike(processed_search_text))
    else:
        raw_books = Book.query.all()

    if serialize:
        raw_books = [b.to_dict for b in raw_books]

    return raw_books


def get_book_by_id(book_id):
    return Book.query.filter_by(id=book_id).first_or_404()


def get_author_by_id(author_id):
    return db.session.query(Author).filter_by(id=author_id).first()


def get_authors_by_id_list(author_ids):
    author_int_ids = [int(i) for i in author_ids]
    return list(db.session.query(Author).filter(Author.id.in_(author_int_ids)).all())


def update_book(book_id, title, genre, author_ids):
    book = Book.query.filter_by(id=book_id).first_or_404()
    book.title = title
    book.genre = genre
    book.authors = get_authors_by_id_list(author_ids)
    db.session.commit()
    return book


def store_book(title, genre, author_ids):
    authors = get_authors_by_id_list(author_ids)
    book = Book(title, genre, authors)
    db.session.add(book)
    db.session.commit()
    return book


def process_search_query(search_text):
    processed_search_text = u"%{0}%".format(search_text)
    if security_validate(processed_search_text):
        return processed_search_text
    else:
        raise ValueError(Res.ERROR_USER_INPUT_FORBID_CHARS)


def security_validate(search_text):
    # so far stub :(
    return True