#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Module which contains the class Items"""

import pygame
import random
from constants import SPRITE_SIZE


class Items:
    """ Class allowing to create and randomly
        position the items in the maze's structure """

    def __init__(self, my_map, img):
        """Constructor that initializes the items"""

        self.img = pygame.image.load(img).convert()
        self.random_x = ""
        self.random_y = ""
        self.maze = my_map
        self.authorized_positions = []
        self.get_authorized_positions()
        self.position()

    # ------------------------------------------------------------------------------------------------------------------

    def get_authorized_positions(self):
        """Method to create a list of authorized positions to place the items"""

        for y, line in enumerate(self.maze.maze_structure):
            for x, character in enumerate(line):
                if character == "P":
                    self.authorized_positions.append((x, y))

    # ------------------------------------------------------------------------------------------------------------------

    def position(self):
        """Method to set a random position from the authorized_positions list"""

        self.random_x, self.random_y = random.choice(self.authorized_positions)
        self.random_x = self.random_x * SPRITE_SIZE
        self.random_y = self.random_y * SPRITE_SIZE
