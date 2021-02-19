#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Hero module which contains the class Hero"""
import pygame
from constants import SPRITE_NUMBER, SPRITE_SIZE, MACGYVER_IMG


class Hero:
    """Class allowing to create the hero of the game:
       MacGyver """

    def __init__(self, structure):
        """Constructor that initializes the hero MacGyver"""
        # MacGyver Sprite
        self.representation = pygame.image.load(MACGYVER_IMG).convert_alpha()
        # initial x and y position of MacGyver
        self.x = 0
        self.y = 0
        # New MacGyver's positions
        self.sprite_x = 0
        self.sprite_y = 0
        self.structure = structure
        self.items_collected = 0

    # ------------------------------------------------------------------------------------------------------------------
    def move(self, direction):
        """Method allowing to move MacGyver"""

        # Move to the right
        if direction == "RIGHT":
            # For not exceeding the screen
            if self.sprite_x < (SPRITE_NUMBER - 1):
                # We verify the destination sprite is not a wall
                if self.structure[self.sprite_y][self.sprite_x + 1] != "W":
                    # Move of one box
                    self.sprite_x += 1
                    # Calculation of the real position in pixel
                    self.x = self.sprite_x * SPRITE_SIZE

        # Move to the left
        if direction == "LEFT":
            if self.sprite_x > 0:
                if self.structure[self.sprite_y][self.sprite_x - 1] != "W":
                    self.sprite_x -= 1
                    self.x = self.sprite_x * SPRITE_SIZE

        # move up
        if direction == "UP":
            if self.sprite_y > 0:
                if self.structure[self.sprite_y - 1][self.sprite_x] != "W":
                    self.sprite_y -= 1
                    self.y = self.sprite_y * SPRITE_SIZE

        # Move down
        if direction == "DOWN":
            if self.sprite_y < (SPRITE_NUMBER - 1):
                if self.structure[self.sprite_y + 1][self.sprite_x] != "W":
                    self.sprite_y += 1
                    self.y = self.sprite_y * SPRITE_SIZE
