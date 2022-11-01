#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Helper script for editing J.B.A topic questions.

jba_topic_question_helper.py
"""


# --------------------
# --IMPORTS
# --------------------
# Standard library modules:
import argparse
import pathlib
import typing


# Third party modules:

# Local scripts and modules:


# --------------------
# --CONSTANTS
# --------------------
# Script possible actions.
ACTION_COPY = "copy"
ACTION_PASTE = "paste"
ACTION_CHOICES = (ACTION_COPY, ACTION_PASTE)
# Supported JBA tracks.
TRACK_CHOICE_FE_CORE = "fe_core"
TRACK_CHOICE_PY_CORE = "py_core"
TRACK_CHOICES = (TRACK_CHOICE_PY_CORE, TRACK_CHOICE_FE_CORE)
# Track solution directories.
TRACK_DIR_BASE = "$HOME/I/JetBrainsAcademy/"
TRACK_DIR_PY_CORE = "python_core/"
TRACK_DIR_FE_CORE = "front_end_core/"
# Track question templates.
TRACK_TEMPLATE_PY_CORE = "jba_py_template.py"


# --------------------
# --DATA TYPES
# --------------------
class QuestionPaths(typing.NamedTuple):
    current_question: pathlib.Path
    solutions_dir: pathlib.Path | None
    question_template: pathlib.Path | None


# --------------------
# --CLASSES
# --------------------


# --------------------
# --FUNCTIONS
# --------------------
def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--track", required=True, choices=TRACK_CHOICES,
        help="The JBA track in which the question appears",
    )
    parser.add_argument(
        "--action", required=True, choices=ACTION_CHOICES,
        help=("The required action, "
              "'paste' new question for editing "
              "or 'copy' the code of a solved question")
    )
    return parser


def parse_args(parser: argparse.ArgumentParser) -> tuple[str, str]:
    args = parser.parse_args()
    return args.track, args.action


def set_up_question_paths(
        question_file_path: str, track: str, action: str
) -> QuestionPaths:
    path_question = pathlib.Path(question_file_path)
    if track == TRACK_CHOICE_PY_CORE:
        path_solutions_dir = get_track_solutions_dir(track, action)
        path_template = get_track_solutions_dir(track, action)
    pass


def main():
    # Set up argparse.
    parser = init_parser()
    # Get invocation info from argparse.
    track, action = parse_args(parser)
    # Set up the relevant path variables for the selected track.
    question_paths = set_up_question_paths(track, action)
    print(track, action)
    pass


# --------------------
# --PROGRAM CODE
# --------------------
if __name__ == "__main__":
    main()
