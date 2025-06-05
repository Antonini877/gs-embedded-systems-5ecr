from utils.colors import Colors
import pygame

def draw_text(screen, text, pos, color=Colors.BLACK):
    font = pygame.font.SysFont(None, 22)
    img = font.render(text, True, color)
    screen.blit(img, pos)