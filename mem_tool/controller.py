import logging

from . import view, model

logger = logging.getLogger(__name__)


def controller(command):
    logger.debug(str(command))
    match command:
        # main menu
        case ["menu", "main"]:
            choice = view.get_menu_choice_main()
            next_command = ["menu_choice", "main", choice]
        case ["menu_choice", "main", "1"]:
            # 1. Add flashcards
            next_command = ["menu", "add_flashcard"]
        case ["menu_choice", "main", "2"]:
            # 2. Practice flashcards
            next_command = ["menu", "practice"]
        case ["menu_choice", "main", "3"]:
            # 3. Exit
            next_command = ["exit"]
        case ["menu_choice", "main", invalid_choice]:
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu", "main"]

        # add_flashcard menu
        case ["menu", "add_flashcard"]:
            choice = view.get_menu_choice_add_flashcards()
            next_command = ["menu_choice", "add_flashcard", choice]
        case ["menu_choice", "add_flashcard", "1"]:
            # 1. Add a new flashcard
            view.flashcard_create()
            next_command = ["menu", "add_flashcard"]
        case ["menu_choice", "add_flashcard", "2"]:
            # 2. Return to main menu
            next_command = ["menu", "main"]
        case ["menu_choice", "add_flashcard", invalid_choice]:
            # invalid choice
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu", "add_flashcard"]

        # practicing flashcards
        case ["menu", "practice"]:
            flashcards = model.get_all_flashcards()
            next_command = ["menu", "practice", flashcards]
        case ["menu", "practice", None]:
            # Handle no flashcards
            view.print_no_flashcards()
            next_command = ["menu", "main"]
        case ["menu", "practice", flashcards]:
            flashcard = flashcards.next()
            next_command = ["menu", "practice", flashcards, flashcard]
        case ["menu", "practice", _, None]:
            # Handle finished flashcards
            next_command = ["menu", "main"]
        case ["menu", "practice", flashcards, flashcard]:
            choice = view.get_menu_choice_practice(flashcard)
            next_command = [
                "menu_choice", "practice", choice, flashcards, flashcard]
        case ["menu_choice", "practice", "y", flashcards, flashcard]:
            # "y" = show answer
            view.flashcard_show_answer(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "practice", "n", flashcards, _]:
            # "n" = don't show answer
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "practice", "u", flashcards, flashcard]:
            # "u" = update
            choice = view.get_menu_choice_update_flashcard()
            next_command = [
                "menu_choice", "practice", "u", choice, flashcards, flashcard]
        case ["menu_choice", "practice", "u", "e", flashcards, flashcard]:
            # "e" = update:edit
            view.flashcard_update_edit(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "practice", "u", "d", flashcards, flashcard]:
            # "d" = update:delete
            view.flashcard_update_delete(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "practice", invalid_choice, flashcards,
              flashcard]:
            # invalid choice (practice menu)
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu", "practice", flashcards, flashcard]
        case ["menu_choice", "practice", "u", invalid_choice,
              flashcards, flashcard]:
            next_command = ["menu_choice", "practice", "u", flashcards,
                            flashcard]
            # invalid choice (update submenu)
            view.print_invalid_menu_choice_error(invalid_choice)

        # exit program
        case ["exit"]:
            view.print_exit_message()
            next_command = None
            exit()

        # catch all for unhandled commands
        case [*unhandled_command]:
            view.print_unhandled_command_message(unhandled_command)
            next_command = ["menu", "main"]

    return next_command
