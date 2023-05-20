_db = []


def add_new_flashcard(flashcard_data):
    _db.append(flashcard_data)


def get_all_flashcards():
    return _db
