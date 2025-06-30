from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Author(Base):
    __tablename__ = 'book_author'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True)
    is_active = Column(Boolean, default=True)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = 'book_book'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author_id = Column(Integer, ForeignKey('author.id'))
    published_date = Column(DateTime)
    price = Column(Numeric(6, 2))
    discount = Column(Numeric(6, 2), default=0)
    book_metadata = Column(JSON, default=dict)

    author = relationship("Author", back_populates="books")
    reviews = relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = 'book_review'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book_book.id'))
    rating = Column(Integer)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    book = relationship("Book", back_populates="reviews")