#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Maze module which contains the class Maze"""

import pygame
import constants as const


class Maze:

    """Class allowing to create and display the game's maze
    started from the maze file"""

    def __init__(self, file):
        """Constructor that initializes the maze"""
        self.file = file
        self.maze_structure = []
        self.items_set = []
        self.items_pos = []
        self.items_nb = 3
        self.x = 0
        self.y = 0
        self.paths = pygame.image.load(const.PATH_IMG).convert()
        self.produce_with_file()
        self.guardian_pos = 0

    # ------------------------------------------------------------------------------------------------------------------

    def produce_with_file(self):
        """Method allowing to produce the labyrinth according to the construction file.
        We create a general list containing a list for each line to display"""
        # Open the file
        with open(const.CONSTRUCTION, "r") as file:

            # Browse file lines
            for lines in file:
                lines_set = []

                # Browse the sprites(letters) contained in the file
                for character in lines:

                    if character != "\n":
                        # Add the sprite to the list of the line
                        lines_set.append(character)
                self.maze_structure.append(lines_set)

    # ------------------------------------------------------------------------------------------------------------------

    def display(self, window):
        """Method allowing to display the plan in function
        of the construction list returned by generate()"""

        # Load the images
        start = pygame.image.load(const.START_IMG).convert()
        walls = pygame.image.load(const.WALL_IMG).convert()
        path = pygame.image.load(const.PATH_IMG).convert()
        arrival = pygame.image.load(const.ARRIVAL_IMG).convert_alpha()

        # Iterate through the level
        for y, lines_set in enumerate(self.maze_structure):
            for x, character in enumerate(lines_set):
                if character == "S":  # S = Start
                    window.blit(start, (x * const.SPRITE_SIZE, y * const.SPRITE_SIZE))
                if character == "W":  # W = Wall
                    window.blit(walls, (x * const.SPRITE_SIZE, y * const.SPRITE_SIZE))
                elif character == "P":  # P = Path
                    window.blit(path, (x * const.SPRITE_SIZE, y * const.SPRITE_SIZE))
                elif character == "A":  # A = Arrival
                    self.guardian_pos = (x * const.SPRITE_SIZE, y * const.SPRITE_SIZE)
                    window.blit(arrival, self.guardian_pos)
