#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Backend -> Django -> Launching server
Topic name: Processing requests
Question name: Movie Ratings
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
    from django.http import HttpResponse, Http404
    from django.views import View
    
    cinema_ratings = {
        "The Dark Knight": 8.2,
        "The Shawshank Redemption": 8.3,
        "Pulp Fiction": 8.1,
    }
    CINEMA_RATINGS = cinema_ratings

    
    class CinemaRatingView(View):
        description = "Cinema ratings list"

        def get(self, request, film, *args, **kwargs):
            if film not in CINEMA_RATINGS:
                raise Http404
            return HttpResponse(f"{CINEMA_RATINGS[film]}")

        def __str__(self):
            return self.description
    # -=- ANSWER CODE END -=-


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
