from Multiplayer import Chess_Game_Multiplayer
from SinglePlayer import Chess_Game_Singleplayer
import pygame
pygame.init()
screen = pygame.display.set_mode((80 * 10 + 90, 80 * 10 + 90))
screen.fill("#826F66")
pygame.display.set_caption("Chess Engine")
Chess = Chess_Game_Singleplayer(screen)
Chess.Play_SinglePlayer()
