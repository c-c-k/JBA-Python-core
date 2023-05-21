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


class Flashcards:
    def __init__(self, flashcards):
        self._flashcards_iterator = iter(flashcards)

    def next(self):
        try:
            flashcard = next(self._flashcards_iterator)
        except StopIteration:
            flashcard = None
        return flashcard


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


def update_flashcard(flashcard, flashcard_data):
    with Session(get_db()) as session:
        flashcard = session.get(Flashcard, flashcard.id)
        for attribute, new_value in flashcard_data.items():
            setattr(flashcard, attribute, new_value)
        session.commit()


def delete_flashcard(flashcard):
    with Session(get_db()) as session:
        session.delete(flashcard)
        session.commit()


def get_all_flashcards():
    with Session(get_db()) as session:
        flashcards = session.query(Flashcard).all()
    if len(flashcards) == 0:
        return None
    return Flashcards(flashcards)
