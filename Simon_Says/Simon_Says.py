import random
import time
import os
import pygame
from constant_values import *

class SimonGame:

    def __init__(self):

        self._game_board = [["G","R"],
                            ["Y","B"]]

        self.colors = "RGBY"

        self.rounds = 3

        self.speed = 2

    def higher_difficulty(self):
        self.rounds += 1

    def generate_play(self):
        simon_picks = []

        for pick in range(self.rounds):
            var = random.choice(self.colors)
            print(var)
            simon_picks.append(var)
            time.sleep(self.speed)
            os.system("cls")

        return simon_picks

    def get_board(self):
        return self._game_board

    def picks(self, win, col, row):
        # player_picks = []
        radius = TILESIZE // 2 - 15
        if self._game_board[col][row] == "G":
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius + 2)
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius)
            pygame.display.update()
        elif self._game_board[col][row] == "R":
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius + 2)
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius)
            pygame.display.update()
        elif self._game_board[col][row] == "Y":
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius + 2)
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius)
            pygame.display.update()
        elif self._game_board[col][row] == "B":
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius + 2)
            pygame.draw.circle(win, WHITE, (col * TILESIZE + TILESIZE // 2, row * TILESIZE + TILESIZE // 2), radius)
            pygame.display.update()
        return self._game_board[col][row]




