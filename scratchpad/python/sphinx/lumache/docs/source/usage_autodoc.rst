Usage with autodoc
==================

.. _usage_autodoc:

Creating recipes
----------------

To retrieve a list of random ingredients you can use the ``lumache_autodoc.get_random_ingredients()`` function:

.. autofunction:: lumache_autodoc.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"`` or ``"veggies"``. Otherwise, :py:func:`lumache_autodoc.get_random_ingredients()` will raise an exception.

.. autoexception:: lumache_autodoc.InvalidKindError

>>> import lumache_autodoc
>>> lumache_autodoc.get_random_ingredients(kind=None)
['shells', 'gorgonzola', 'parsley']