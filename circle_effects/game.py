import math
import random
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

    self.radius = int(self.width / 2)
    self.increment_radius = False
    self.circle_points = []
    self.red = 255
    self.blue = 0
    self.green = 0
    self.incrementer = 1
    self.set_points()

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

  def set_points(self):
    cx = int(self.width / 2)
    cy = int(self.height / 2)
    for point in range(0, 180):
      angle = random.randrange(0, 360)
      _radius = random.randrange(0, self.radius)
      angle_degrees = math.radians(angle)
      x = int(cx + math.sin(angle_degrees) * self.radius)
      y = int(cy - math.cos(angle_degrees) * self.radius)
      self.circle_points.append((x,y,_radius,angle))

  def update_points(self):
    count = 0
    cx = int(self.width / 2)
    cy = int(self.height / 2)
    for point in self.circle_points:
      self.incrementer += 1
      if self.incrementer > 500:
        self.incrementer = 1
      if self.incrementer % 30 == 0:
        if self.red > 0:
          self.red -= 1
          if self.red == 120:
            self.green = 255
        elif self.green > 0:
          self.green -= 1
          if self.green == 120:
            self.blue = 255
        elif self.blue > 0:
          self.blue -= 1
          if self.blue == 120:
            self.red = 255
      _angle = point[3]
      _radius = point[2]
      _radius -= 1
      if _radius == 0:
        _radius = self.radius
      x = int(cx + math.sin(_angle) * _radius)
      y = int(cy - math.cos(_angle) * _radius)
      self.circle_points[count] = (x,y,_radius,_angle)
      count += 1

  def draw(self):
    for point in self.circle_points:
      self.screen.set_at((point[0], point[1]), (self.red, self.green, self.blue))

  def run(self):
    while self.running:
      self.clock.tick(60)
      self.handle_input()
      self.update_points()
      self.screen.fill(self.bg_color)
      self.draw()
      pygame.display.flip()
