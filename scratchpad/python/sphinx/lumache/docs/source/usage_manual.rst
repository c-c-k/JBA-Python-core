Usage without autodoc (i.e. manual)
===================================

.. _usage_manual:

Creating recipes
----------------

To retrieve a list of random ingredients you can use the ``lumache_manual.get_random_ingredients()`` function:

.. py:function:: lumache_manual.get_random_ingredients(kind=None)

    Return a list of random ingredients as a strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None.
    :raise lumache_manual.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

The ``kind`` parameter should be either ``"meat"``, ``"fish"`` or ``"veggies"``. Otherwise, :py:func:`lumache_manual.get_random_ingredients()` will raise an exception.

.. py:exception:: lumache_manual.InvalidKindError

Raised if kind is invalid.

>>> import lumache_manual
>>> lumache.get_random_ingredients(kind=None)
['shells', 'gorgonzola', 'parsley']