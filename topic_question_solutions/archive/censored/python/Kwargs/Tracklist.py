#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Python -> Control flow -> Functions -> Arguments
Topic name: Kwargs
Question name: Tracklist
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
"""
# -=- QUESTION SOLUTION -=-
import io
import sys


def main():
    _tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                           "On the Other Side": "Samara"},
               "Cure": {"Disintegration": "Lovesong",
                        "Wish": "Friday I'm in love"}}

    # -=- ANSWER CODE START -=-
    def tracklist(**bands):
        for band, tracks in bands.items():
            print(band)
            for album, track in tracks.items():
                print(f"ALBUM: {album} TRACK: {track}")
        pass

    # -=- ANSWER CODE END -=-
    tracklist(**_tracks)


input_ = []
sys.argv = ["arg_0"].extend(input_)
sys.stdin = io.StringIO("\n".join(input_))
main()
# -=- SAMPLE IO -=-
SAMPLE_IO = """

"""
