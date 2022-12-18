#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Basics -> Builtins
Topic name: Map and filter
Question name: Analyzing exam results
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
    scores_maths = [100, 75, 90, 95, 60, 50, 95, 85, 70, 75,
                    90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                    50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                    95, 45, 60, 45, 80, 70, 55, 45, 60, 90]
    
    scores_physics = [50, 65, 85, 100, 60, 55, 90, 85, 70, 90,
                      50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                      60, 90, 40, 90, 95, 90, 80, 95, 85, 80,
                      95, 90, 75, 50, 80, 70, 50, 35, 65, 90]
    
    scores_english = [50, 40, 100, 45, 95, 70, 75, 60, 50, 100,
                      50, 45, 35, 100, 95, 90, 85, 90, 80, 85,
                      90, 85, 60, 45, 100, 70, 65, 50, 55, 95,
                      50, 65, 85, 100, 60, 55, 90, 85, 70, 90]
    
    overall_scores = list(map(lambda x, y, z: x + y + z, scores_english,
                              scores_physics,
                              scores_maths))
    
    admitted_students = list(filter(lambda x: x >= 270, overall_scores))
    
    print(len(admitted_students))
    # -=- ANSWER CODE END -=-
    print(len([
        scores
        for scores
        in zip(scores_maths, scores_physics, scores_english)
        if sum(scores) >= 270
    ]))
    print(*(
        len(subject)
        for subject
        in (scores_maths, scores_physics, scores_english)))


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
