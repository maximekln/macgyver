#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
##################### MAZEGYVER ###########################
#                                                         #
#  2D Game in which we move MacGyver through a labyrinth. #
#  MacGyver has to collect several items in order to  put #
#  the guardian to sleep and escape the labyrinth.        #
#                                                         #
###########################################################
"""

from adventure import Adventure

if __name__ == "__main__":
    adventure = Adventure()

    while True:

        if adventure.welcome_screen:
            adventure.operate_welcome_screen()
        elif adventure.adventure_screen:
            adventure.operate_adventure_screen()
        elif adventure.adventure_end_screen:
            adventure.operate_adventure_end_screen()
        else:
            break
