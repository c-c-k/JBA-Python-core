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
            # 1. Enter add flashcards menu
            next_command = ["menu", "add_flashcard"]
        case ["menu_choice", "main", "2"]:
            # 2. Enter practice flashcards menu
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
            # "y" = Enter learning menu
            next_command = ["menu", "learning", flashcards, flashcard]
        case ["menu_choice", "practice", "n", flashcards, _]:
            # "n" = skip flashcard
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "practice", "u", flashcards, flashcard]:
            # "u" = Enter update menu
            next_command = ["menu", "update_flashcards", flashcards, flashcard]
        case ["menu_choice", "practice", invalid_choice, flashcards,
              flashcard]:
            # invalid choice (practice menu)
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu", "practice", flashcards, flashcard]

        # flashcard update menu
        case ["menu", "update_flashcards", flashcards, flashcard]:
            choice = view.get_menu_choice_update_flashcard()
            next_command = [
                "menu_choice", "update_flashcards", choice,
                flashcards, flashcard]
        case ["menu_choice", "update_flashcards", "e", flashcards, flashcard]:
            # "e" = update:edit
            view.flashcard_update_edit(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "update_flashcards", "d", flashcards, flashcard]:
            # "d" = update:delete
            view.flashcard_update_delete(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "update_flashcards", invalid_choice,
              flashcards, flashcard]:
            # invalid choice
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu_choice", "update_flashcards",
                            flashcards, flashcard]

        # learning menu
        case ["menu", "learning", flashcards, flashcard]:
            choice = view.get_menu_choice_learning(flashcard)
            next_command = [
                "menu_choice", "learning", choice,
                flashcards, flashcard]
        case ["menu_choice", "learning", "y", flashcards, flashcard]:
            # "y" = correct answer
            model.flashcard_add_correct_answer(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "learning", "n", flashcards, flashcard]:
            # "n" = wrong_answer
            model.flashcard_add_wrong_answer(flashcard)
            next_command = ["menu", "practice", flashcards]
        case ["menu_choice", "learning", invalid_choice,
              flashcards, flashcard]:
            # invalid choice
            view.print_invalid_menu_choice_error(invalid_choice)
            next_command = ["menu_choice", "learning",
                            flashcards, flashcard]

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
