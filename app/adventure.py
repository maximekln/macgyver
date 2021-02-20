#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""Adventure module which contains the class Adventure"""


import pygame
import constants as const
from maze import Maze
from hero import Hero
from items import Items


class Adventure:
    """
    # Class allowing to define methods to operate the three main sections of the game :
    # - welcome screen ;
    # - adventure screen ;
    # - adventure end screen ;
    """

    def __init__(self):
        """Constructor that initializes the adventure"""
        pygame.init()
        pygame.font.init()
        pygame.time.Clock().tick(30)  # Speed loop limit
        self.font_ka1 = pygame.font.Font(const.FONT_IMG, 25)
        self.welcome_screen = True
        self.adventure_screen = False
        self.adventure_end_screen = False
        self.macgyver = ""

    # ------------------------------------------------------------------------------------------------------------------

    def operate_welcome_screen(self):
        """Method to make the welcome screen work"""

        # Displays window
        window = pygame.display.set_mode((const.MAZE_SIZE, const.MAZE_SIZE))
        # Displays title of the game
        pygame.display.set_caption(const.GAME_TITLE)

        # Loads and displays welcome screen
        welcome_screen = pygame.image.load(const.ADVENTURE_MENU_IMG).convert()
        welcome_screen = pygame.transform.scale(welcome_screen, (const.MAZE_SIZE, const.MAZE_SIZE))
        window.blit(welcome_screen, (0, 0))  # Draws welcome screen in window
        pygame.display.set_caption(const.GAME_TITLE)  # Title of the game

        # Loads and plays continuously WELCOME_SOUND with adjusted volume
        pygame.mixer.music.load(const.WELCOME_SOUND)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0.2)

        # Refresh
        pygame.display.flip()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    self.welcome_screen = False
                    self.adventure_screen = False
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.welcome_screen = False
                    self.adventure_screen = True
                    pygame.mixer.music.stop()
                    return False
                pygame.display.flip()

    # ------------------------------------------------------------------------------------------------------------------

    def operate_adventure_screen(self):
        """Method to make the adventure screen of the game work"""

        window = pygame.display.set_mode((const.MAZE_SIZE, (const.MAZE_HEIGHT + const.BANNER_HEIGHT)))
        pygame.display.set_caption(const.GAME_TITLE)  # Title of the window

        # Initializing the map
        maze = Maze(const.CONSTRUCTION)
        maze.display(window)

        # Initializing the hero
        macgyver_image = pygame.image.load(const.MACGYVER_IMG).convert()

        # Initializing the items
        images = [const.NEEDLE_IMG, const.ETHER_IMG, const.PLASTIC_TUBE_IMG]
        items_list = list()

        for img in images:
            items = Items(maze, img)
            items_list.append(items)

        # Initializing the hero
        self.macgyver = Hero(maze.maze_structure)

        # Loads and plays continuously ADVENTURE_SOUND with adjusted volume
        pygame.mixer.music.load(const.ADVENTURE_SOUND)
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.rewind()
        pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0.3)

        pygame.display.flip()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.adventure_screen = False
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.adventure_screen = False
                    self.welcome_screen = True
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.welcome_screen = False
                    self.adventure_screen = True
                    return False

                # Hero's movements with keyboard
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.macgyver.move("RIGHT")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.macgyver.move("LEFT")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.macgyver.move("DOWN")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.macgyver.move("UP")

            window.blit(maze.paths, (0, 0))
            maze.display(window)

            # Displays the items randomly
            for item in items_list:
                window.blit(item.img, (item.random_x, item.random_y))

                # Displays the hero
            window.blit(macgyver_image, (self.macgyver.x, self.macgyver.y))

            # Banner with the counter
            banner = pygame.Surface((const.MAZE_SIZE, const.BANNER_HEIGHT))
            banner.fill((255, 165,  0))
            window.blit(banner, (0, const.MAZE_HEIGHT))
            text = self.font_ka1.render(
                "ITEMS COLLECTED : " + str(self.macgyver.items_collected),
                False,
                (255, 255, 0))
            window.blit(text, (40, 500))

            pygame.display.flip()

            # Removes the item from items_list when macgyver passes over it
            for item in items_list:
                if (item.random_x, item.random_y) == (self.macgyver.x, self.macgyver.y):
                    items_list.remove(item)
                    # Increment the inventory value every time hero collects an item
                    self.macgyver.items_collected += 1

            # When macgyver meets the guardian, game is over
            if (self.macgyver.x, self.macgyver.y) == maze.guardian_pos:
                self.adventure_end_screen = True
                self.adventure_screen = False
                pygame.mixer.music.stop()
                return False

    # ------------------------------------------------------------------------------------------------------------------

    def operate_adventure_end_screen(self):
        """Method to make the end_screen of the game work : be it a victory or a defeat"""

        while True:

            # If the player has collected all the items : MacGyver wins
            if self.macgyver.items_collected == 3:
                window = pygame.display.set_mode((const.MAZE_SIZE, const.MAZE_SIZE))
                pygame.display.set_caption("YOU ARE FREE ! WELL DONE MACGYVER !")
                end_page = pygame.image.load(const.WIN_IMG).convert()
                window.blit(pygame.transform.scale(end_page, (const.MAZE_SIZE, const.MAZE_SIZE)), (0, 0))

                # Loads and plays WIN_SOUND with adjusted volume
                pygame.mixer.music.load(const.WIN_SOUND)
                pygame.mixer.music.play()
                pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(0.1)

                pygame.display.flip()

                # If the player has one or more items missing : macgyver loses
            elif self.macgyver.items_collected < 3:
                window = pygame.display.set_mode((const.MAZE_SIZE, const.MAZE_SIZE))
                pygame.display.set_caption("YOU LOSE ! MACGYVER IS GONE... ")
                end_page = pygame.image.load(const.GAME_OVER_IMG).convert()
                window.blit(pygame.transform.scale(end_page, (const.MAZE_SIZE, const.MAZE_SIZE)), (0, 0))

                # Loads and plays LOSE_SOUND with adjusted volume
                pygame.mixer.music.load(const.LOSE_SOUND)
                pygame.mixer.music.play()
                pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(0.2)

                pygame.display.flip()

            while self.adventure_end_screen:
                for event in pygame.event.get():
                    # Back to the welcome screen.
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                        self.welcome_screen = True
                        self.adventure_end_screen = False
                        pygame.mixer.music.stop()
                        return False
