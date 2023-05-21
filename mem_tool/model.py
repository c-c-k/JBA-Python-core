from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DB_URI = "sqlite:///flashcard.db?check_same_thread=False"
_db = None


DeclarativeBase = declarative_base()


class Flashcard(DeclarativeBase):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


def get_db():
    global _db
    if _db is None:
        _db = create_engine(DB_URI)
    return _db


def init_db():
    DeclarativeBase.metadata.create_all(get_db())


def add_new_flashcard(flashcard_data):
    with Session(get_db()) as session:
        _flashcard = Flashcard(
            question=flashcard_data['question'],
            answer=flashcard_data['answer']
        )
        session.add(_flashcard)
        session.commit()


def get_all_flashcards():
    with Session(get_db()) as session:
        _flashcards = session.query(Flashcard).all()
    return _flashcards
