def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as a strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None.
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    # return ['eggs', 'bacon', 'spam']
    if kind is None:
        return ['shells', 'gorgonzola', 'parsley']


class InvalidKindError(Exception):
    """Raised if kind is invalid."""
    pass
