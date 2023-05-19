#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Templates
Topic name: Rendering templates
Question name: Page of a book
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from django.views.generic.base import TemplateView
    
    book = {
        'Page 1': 'This is the cat',
        'Page 2': 'That killed the rat',
        'Page 3': 'That ate the malt',
        'Page 4': 'That lay in the house that Jack built.',
    }
    
    
    class PageView(TemplateView):
        template_name = "book/page.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            n_page = kwargs['n_page']
            context['content'] = book["Page " + n_page]
            return context
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
