import pygame
from constant_values import *
from Simon_Says import *


class Game:
    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

        self.gameimage = pygame.image.load("icon/icon.png")

        pygame.display.set_caption("Simon Says")

        pygame.display.set_icon(self.gameimage)

        self.clock = pygame.time.Clock()

        self.running = True

        self.simon = SimonGame()

        self.click = 0

        self.player_pick = []

        self.comp_picks = None

    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = y // TILESIZE
        col = x // TILESIZE
        return row, col

    def new(self):

        self.playing = True

        self.RGBY()

        self.comp_picks = self.simon.generate_play()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = self.get_row_col_from_mouse(pos)
                self.player_pick.append(self.simon.picks(self.window, col, row))
                self.click += 1
                print(self.player_pick)

            if self.comp_picks == self.player_pick and self.click == self.simon.rounds:
                self.simon.rounds += 1
                self.simon.speed -= 0.2
                self.player_pick = []
                self.comp_picks = None
                self.click = 0
                self.new()

            if self.comp_picks != self.player_pick and self.click == self.simon.rounds:
                print(" Game Over Thanks for Playing")
                pygame.quit()

    def RGBY(self):
        for y, row in enumerate(self.simon.get_board()):
            for x, col in enumerate(row):
                if col == "G":
                    pygame.draw.rect(self.window, GREEN, (y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE))
                if col == "R":
                    pygame.draw.rect(self.window, RED, (y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE))
                if col == "Y":
                    pygame.draw.rect(self.window, YELLOW, (y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE))
                if col == "B":
                    pygame.draw.rect(self.window, BLUE, (y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE))


        self.clock.tick(FPS)
        pygame.display.update()


    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK)
        self.RGBY()

        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.running:
            self.event()
            self.update()
            self.draw()
        self.running = False

    # def game_over(self, p_picks, comp_pics):
    #     if p_picks != c

    def intro_screen(self):
        pass


play = Game()
play.new()
while play.running:
    play.main()


pygame.quit()



