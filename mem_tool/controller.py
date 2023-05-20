import logging

from . import view, model

logger = logging.getLogger(__name__)


def controller(command):
    logger.debug(str(command))
    match command:
        # main menu
        case ["print", "menu", "main"]:
            choice = view.get_menu_choice_main()
            next_command = ["menu_choice", "main", choice]
        case ["menu_choice", "main", "1"]:
            # 1. Add flashcards
            next_command = ["print", "menu", "add_flashcard"]
        case ["menu_choice", "main", "2"]:
            # 2. Practice flashcards
            next_command = ["practice"]
        case ["menu_choice", "main", "3"]:
            # 3. Exit
            next_command = ["exit"]
        case ["menu_choice", "main", invalid_choice]:
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["print", "menu", "main"]

        # add_flashcard menu
        case ["print", "menu", "add_flashcard"]:
            choice = view.get_menu_choice_add_flashcards()
            next_command = ["menu_choice", "add_flashcard", choice]
        case ["menu_choice", "add_flashcard", "1"]:
            # 1. Add a new flashcard
            next_command = ["crud", "create", "flashcard"]
        case ["menu_choice", "add_flashcard", "2"]:
            # 2. Return to main menu
            next_command = ["print", "menu", "main"]
        case ["menu_choice", "add_flashcard", invalid_choice]:
            # invalid choice
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["print", "menu", "add_flashcard"]

        # adding a new flashcard
        case ["crud", "create", "flashcard"]:
            flashcard_data = view.get_flashcard_data()
            model.add_new_flashcard(flashcard_data)
            # redirect back to add flashcard menu
            next_command = ["print", "menu", "add_flashcard"]

        # practicing flashcards
        case ["practice"]:
            flashcards = model.get_all_flashcards()
            next_command = ["practice", flashcards]
        case ["practice", flashcards] if len(flashcards) == 0:
            view.print_no_flashcards()
            next_command = ["print", "menu", "main"]
        case ["practice", flashcards]:
            view.practice_flashcards(flashcards)
            next_command = ["print", "menu", "main"]

        # exit program
        case ["exit"]:
            view.print_exit_message()
            next_command = None
            exit()

        # catch all for unhandled commands
        case [*unhandled_command]:
            view.print_unhandled_command_message(unhandled_command)
            next_command = ["print", "menu", "main"]

    return next_command

