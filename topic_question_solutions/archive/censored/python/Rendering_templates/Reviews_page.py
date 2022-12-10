#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Templates
Topic name: Rendering templates
Question name: Reviews page
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    # -=- ANSWER CODE START -=-
    from django.shortcuts import render
    from django.views import View
    
    
    class ReviewView(View):
        reviews = ['That book was supercalifragilisticexpialidocious', 'It was a ok, I guess']
    
        def get(self, request, *args, **kwargs):
            context = {'reviews': self.reviews}
            return render(request, 'book/reviews.html', context )
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
