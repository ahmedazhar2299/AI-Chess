from Multiplayer import Chess_Game_Multiplayer
from SinglePlayer import Chess_Game_Singleplayer
import pygame
import pygame

SIZE = 80 * 10 + 90
WIN = pygame.display.set_mode((SIZE, SIZE))


class StartScreen:
    def __init__(self):
        self.__rect1 = None
        self.__rect2 = None

    def main(self):

        title1 = "GIRAFFE"
        title2 = "CHESS"
        color1 = pygame.Color((236, 155, 59))
        color2 = pygame.Color((242, 76, 76))
        pygame.font.init()
        base_font2 = pygame.font.SysFont("cambriamath", 150)
        base_font1 = pygame.font.SysFont("consolas", 40)

        t1 = base_font1.render(title1, True, color2)
        t2 = base_font2.render(title2, True, color1)

        WIN.blit(t1, (int(SIZE/3) - 55, 100))
        WIN.blit(t2, (int(SIZE/4), 110))

        image1 = pygame.image.load(r'./images/main.png').convert_alpha()
        image1 = pygame.transform.scale(image1, (130, 70))
        WIN.blit(image1, (int(SIZE / 2 + 80), 65))

        image2 = pygame.image.load(r'./images/logo.png').convert_alpha()
        image2 = pygame.transform.scale(image2, (500, 500))
        WIN.blit(image2, (int(SIZE / 3), 270))

    def control_button(self):

        # color1 = pygame.Color((236, 155, 59))
        color2 = pygame.Color((242, 128, 128))
        pygame.font.init()
        base_font1 = pygame.font.SysFont("consolas", 25)

        t1 = base_font1.render("VS CPU", True, color2)
        self.__rect1 = pygame.Rect(150, 350, 110, 50)
        pygame.draw.rect(WIN, (255, 0, 244), self.__rect1, 2)
        WIN.blit(t1, (self.__rect1.x + 10, self.__rect1.y + 13))

        t2 = base_font1.render("MULTIPLAYER", True, color2)
        self.__rect2 = pygame.Rect(150, 420, 180, 50)
        pygame.draw.rect(WIN, (255, 0, 244), self.__rect2, 2)
        WIN.blit(t2, (self.__rect2.x + 10, self.__rect2.y + 13))

    def start(self):
        pygame.init()
        # SIZE = 80 * 9 + 90
        # WIN = pygame.display.set_mode((SIZE, SIZE))
        pygame.display.set_caption("Game Start Screen")
        WIN.fill(0x000)

        pygame.display.flip()
        GAME_SCREEN = True

        image = pygame.image.load(r'./images/bg.png').convert_alpha()
        image = pygame.transform.scale(image, (SIZE, SIZE))
        # image.set_colorkey((0, 0, 0))
        image.set_alpha(50)
        WIN.blit(image, (0, 0))

        while GAME_SCREEN:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    GAME_SCREEN = False
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__rect1.collidepoint(event.pos):
                        return "SinglePlayer"
                    if self.__rect2.collidepoint(event.pos):
                        return "MultiPlayer"


                self.main()
                self.control_button()

                pygame.display.update()


option = StartScreen().start()
if option == "SinglePlayer":
    pygame.init()
    screen = pygame.display.set_mode((80 * 10 + 90, 80 * 10 + 90))
    screen.fill("#826F66")
    pygame.display.set_caption("Chess Engine")
    Chess = Chess_Game_Singleplayer(screen)
    Chess.Play_SinglePlayer()
    pygame.display.quit()

elif option == "MultiPlayer":
    pygame.init()
    screen = pygame.display.set_mode((80 * 10 + 90, 80 * 10 + 90))
    screen.fill("#826F66")
    pygame.display.set_caption("Chess Engine")
    Chess = Chess_Game_Multiplayer(screen)
    Chess.Play_Multiplayer()
    pygame.display.quit()
