import pygame
import sys
from pygame.locals import *

class Game():
  def __init__(self, title, width, height, bg_color) -> None:
    self.title = title
    self.width = width
    self.height = height
    self.bg_color = bg_color
    self.screen, self.background = self.create_window()
    self.clock = pygame.time.Clock()
    self.screen.blit(self.background, (0,0))
    self.running = True
    pygame.init()

  def create_window(self):
    """ return screen and background objects """
    screen = pygame.display.set_mode(
      (self.width,self.height),
      HWSURFACE|DOUBLEBUF)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(self.bg_color)
    screen.blit(background, (0,0))
    pygame.display.flip()
    screen.fill(self.bg_color)
    pygame.display.set_caption(self.title)
    return screen, background

  def handle_input(self):
    """ handle events and keypresses """
    for event in pygame.event.get():
      if event.type == QUIT:
        return

    keys = pygame.key.get_pressed()
    if keys[pygame.K_END] or keys[pygame.K_ESCAPE]:
      sys.exit(0)
  
  def run(self):
    while self.running:
      self.handle_input()
      self.screen.fill(self.bg_color)
      pygame.display.flip()
