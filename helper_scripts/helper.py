#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Helper script for editing J.B.A topic questions and projects.

This script executes a number of frequently used helper actions
for solving J.B.A. topic questions and projects.
It is meant to be invoked by an IDE shortcut that executes an external
program on the currently edited file.
The IDE should pass the file path and required action to this script.
The currently implemented actions are:
  - Paste question text copied from the J.B.A. site into the currently
   edited question file (NOTE: The X selection used here is the PRIMARY
   selection, that is highlighted text and not <C-V>).
  - Copy the currently edited question's solution code to the clipboard
   (NOTE: The X selection used here is the clipboard selection,
   that is <C-C> and not highlighted text ).
"""


# --------------------
# --IMPORTS
# --------------------
# Standard library modules:
import argparse
import os
import pathlib
import re
import string
import subprocess


# Third party modules:

# Local scripts and modules:


# --------------------
# --CONSTANTS
# --------------------
# Script possible actions.
ACTION_QUESTION_COPY = "question_copy"
ACTION_QUESTION_PASTE = "question_paste"
ACTION_CHOICES = (ACTION_QUESTION_COPY, ACTION_QUESTION_PASTE)
# Primary execution mode related.
PRIMARY_MODE_QUESTION = "primary_mode_question"
PRIMARY_MODE_QUESTION_ACTIONS = (
    ACTION_QUESTION_COPY, ACTION_QUESTION_PASTE)
PRIMARY_MODE_PROJECT = "primary_mode_project"
PRIMARY_MODE_PROJECT_ACTIONS = ()
# Supported programing languages.
LANGUAGE_PYTHON = "lang_python"
# General script directories.
DIR_ROOT = pathlib.Path(__file__).resolve().parents[1]
# Per programing language solution archives.
DIR_QUESTIONS_BASE = os.path.join(
    DIR_ROOT, "topic_question_solutions/")
DIR_QUESTIONS_PYTHON = os.path.join(
    DIR_QUESTIONS_BASE, "python/")
# Per programing language current solution file.
DIR_QUESTIONS_CURRENT_BASE = os.path.join(
    DIR_QUESTIONS_BASE, "current/")
PATH_QUESTIONS_CURRENT_PYTHON = os.path.join(
    DIR_QUESTIONS_CURRENT_BASE, "python.py")
# Per programing language solution template file.
DIR_TEMPLATE_BASE = os.path.join(
    DIR_ROOT, "helper_scripts/answer_templates/")
PATH_TEMPLATE_PYTHON = os.path.join(
    DIR_TEMPLATE_BASE, "python.py")


# --------------------
# --REGEX
# --------------------
re_question_name_archive = re.compile(r"^Question name: (.+)\n", re.MULTILINE)
re_question_topic_archive = re.compile(r"^Topic name: (.+)\n", re.MULTILINE)
re_question_element_extractor = re.compile(
    (
        r"(?P<TOPIC_CATEGORY>.+)\n"
        r"(?P<TOPIC_NAME>.+)\n"
        r"(?:Topic repetition\n)?"
        r"(?P<QUESTION_NAME>.+?)(?: Problem of the day)?\n"
        r"(?:Next problem in.+\n)?"
        r"(?P<QUESTION_RATING>Easy|Medium|Hard)\n"
        r"\d+ user.+\n"
        r"(?P<QUESTION_BODY>(?:.*\n)+?)"
        r"Report a typo\n"
        r"(?P<SAMPLE_IO>(?:.*\n)*?)"
        r"Write a program\n"
        r"(?:.*\n)+?"
        r"^1\n(?:^\d+\n)*"
        r"(?P<QUESTION_SOLUTION>(?s:.*))"
    ), re.MULTILINE)
re_topic_category_spliter = re.compile("[A-Z][a-z0-9 ]*")


# --------------------
# --DATA TYPES
# --------------------


# --------------------
# --CLASSES
# --------------------


# --------------------
# --FUNCTIONS
# --------------------
def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file", required=True,
        help="The path to the source/target file for the required action",
    )
    parser.add_argument(
        "--action", required=True, choices=ACTION_CHOICES,
        help="The required action.",
    )
    return parser


def parse_args(parser: argparse.ArgumentParser) -> tuple[str, str]:
    args = parser.parse_args()
    return args.file, args.action


def get_primary_execution_mode(action: str) -> str:
    if action in PRIMARY_MODE_QUESTION_ACTIONS:
        return PRIMARY_MODE_QUESTION
    elif action in PRIMARY_MODE_PROJECT_ACTIONS:
        return PRIMARY_MODE_PROJECT
    else:
        raise ValueError(f"Requested action '{action}' doesn't match "
                         "any primary execution mode.")


def get_language(question_file: str) -> str:
    if question_file == PATH_QUESTIONS_CURRENT_PYTHON:
        return LANGUAGE_PYTHON
    else:
        print(question_file, PATH_QUESTIONS_CURRENT_PYTHON, sep="\n")
        raise ValueError(f"File path '{question_file}' doesn't match "
                         "any of the question solution editing file paths.")


def get_question_archive_base_dir(language: str) -> str:
    if language == LANGUAGE_PYTHON:
        return DIR_QUESTIONS_PYTHON
    else:
        raise ValueError(f"Language '{language}' doesn't have "
                         "a question archive directory.")


def get_answer_base_text(language: str) -> str:
    if language == LANGUAGE_PYTHON:
        template_path = PATH_TEMPLATE_PYTHON
    else:
        raise ValueError(f"Language '{language}' doesn't have "
                         "an answer template.")
    return pathlib.Path(template_path).read_text()


def get_archive_names_from_text(
        question_text: str) -> tuple[str | None, str | None]:
    name_match = re_question_name_archive.search(question_text)
    topic_match = re_question_topic_archive.search(question_text)
    name = (name_match.group(1) if name_match else None)
    topic_name = (topic_match.group(1) if name_match else None)
    return name, topic_name


def normalize_name(name: str | None) -> str | None:
    """Change all non ascii alphanumeric characters to underscores."""
    if name is None:
        return None
    valid_chars = string.ascii_letters + string.digits
    name = "".join((char if char in valid_chars else "_" for char in name))
    if name.strip("_") == "":
        return None
    return name


def build_pobj_topic_dir(
        topic_name: str | None, language: str) -> pathlib.Path:
    topic_name = normalize_name(topic_name)
    if topic_name is None:
        topic_name = "unknown_topic"
    if language == LANGUAGE_PYTHON:
        topic_base_dir = DIR_QUESTIONS_PYTHON
    else:
        raise ValueError(f"Unsupported language: '{language}'")
    pobj_topic_dir = pathlib.Path(topic_base_dir, topic_name)
    pobj_topic_dir.mkdir(parents=True, exist_ok=True)
    return pobj_topic_dir


def build_pobj_archive_file(
        name: str | None, pobj_topic_dir: pathlib.Path, language: str
) -> pathlib.Path:
    name = normalize_name(name)
    if name is None:
        next_nameless_question_id = 1 + len(
            [file.name for file in pobj_topic_dir.glob("question_*")])
        name = (
            f"question_{next_nameless_question_id:0>3}"
        )
    if language == LANGUAGE_PYTHON:
        suffix = ".py"
    else:
        raise ValueError(f"Unsupported language: '{language}'")
    return pobj_topic_dir.joinpath(name + suffix)


def archive_previous_question(
        pobj_question_file: pathlib.Path, language: str):
    # Read the questions text from the question file to deduce from it
    # the name and topic subdirectory for the question's archive file.
    question_text = pobj_question_file.read_text()
    # Handle edge case where the file was manually emptied
    # or is otherwise empty.
    if question_text.strip() == "":
        return
    # extract question and topic names from the question's text.
    name, topic_name = get_archive_names_from_text(question_text)
    # construct full archive path from question and topic names.
    pobj_topic_dir = build_pobj_topic_dir(topic_name, language)
    pobj_archive_file = build_pobj_archive_file(name, pobj_topic_dir, language)
    pobj_archive_file.write_text(question_text)


def get_primary_x_selection_text() -> str:
    x_selection_pipe = subprocess.Popen(
        ["xsel", "--primary", "--output"], stdout=subprocess.PIPE)
    question_text = x_selection_pipe.stdout.read()
    # exit_status = x_selection_pipe.wait()
    x_selection_pipe.stdout.close()
    return question_text.decode()


def set_clipboard_x_selection_text(text: str):
    x_selection_pipe = subprocess.Popen(
        ["xsel", "--clipboard", "--input"], stdin=subprocess.PIPE)
    x_selection_pipe.stdin.write(text.encode())
    x_selection_pipe.stdin.close()
    # exit_status = x_selection_pipe.wait()


def extract_substitution_elements(
        question_text: str):  # -> dict[str, str]:
    match = re_question_element_extractor.match(question_text)
    substitution_dict = match.groupdict()
    topic_category = substitution_dict["TOPIC_CATEGORY"]
    topic_category = re_topic_category_spliter.findall(topic_category)
    topic_category = " -> ".join(topic_category)
    substitution_dict["TOPIC_CATEGORY"] = topic_category
    return substitution_dict


def execute_question_paste(
        question_file: str, language: str):
    # Create a pathlib Path object for the current question file
    # for use in the following steps.
    pobj_question_file = pathlib.Path(question_file)
    # Archive the previously edited question.
    archive_previous_question(pobj_question_file, language)
    # Read the new question's text from the X primary selection.
    question_text = get_primary_x_selection_text()
    # Extract the question's elements from the question's text:
    substitution_dict = extract_substitution_elements(question_text)
    # Get base question text from the answer template
    # for the given programing language.
    question_text = get_answer_base_text(language)
    # Format the question's text.
    question_text = string.Template(
        question_text).safe_substitute(substitution_dict)
    # overwrite the old questions text in the current question file
    # with the formatted text of the new question.
    pobj_question_file.write_text(question_text)


def execute_question_mode(question_file: str, action: str):
    # Use the file path to deduce the question's programing language.
    language = get_language(question_file)
    # Execute the selected action:
    if action == ACTION_QUESTION_COPY:
        pass
    if action == ACTION_QUESTION_PASTE:
        execute_question_paste(question_file, language)
    else:
        raise ValueError(f"Unsupported action '{action}'")


def main():
    # Set up argparse.
    parser = init_parser()
    # Get invocation info from argparse.
    question_file, action = parse_args(parser)
    # Fully resolve question file path so that
    # it would match the constant file paths.
    question_file = pathlib.Path(question_file).resolve().as_posix()
    # Choose primary execution mode (question or project).
    primary_execution_mode = get_primary_execution_mode(action)
    # Branch program flow to chosen primary execution mode.
    if primary_execution_mode == PRIMARY_MODE_QUESTION:
        execute_question_mode(question_file, action)
    elif primary_execution_mode == PRIMARY_MODE_PROJECT:
        pass  # TODO


# --------------------
# --PROGRAM CODE
# --------------------
if __name__ == "__main__":
    main()
