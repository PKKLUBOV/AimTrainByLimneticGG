import pygame, random, math, sys


class AimBall:

  def __init__(self, x, y, radius, type_, born_tick):
    self.x = x
    self.y = y

    self.radius = radius
    self.current_radius = 1

    self.type = type_
    self.born_tick = born_tick

  def draw(self):
    global score
    pygame.draw.circle(sc, self.type, (self.x, self.y), self.current_radius)
    if self.current_radius < self.radius:
      self.current_radius += 1

    if math.hypot(xm - self.x, ym - self.y) <= self.current_radius:
      if LKM and self.type == 'red' or PKM and self.type == 'blue':
        score += 1
        print(score)
        AimBalls.remove(self)
      

def spawnAimBalls(count):
  global AimBalls
  for _ in range(count):
    AimBalls.append(
        AimBall(
            random.randint(2, w - 2),  #x
            random.randint(2, h - 2),  #y
            random.randint(15, 30),  #r
            random.choice(['red', 'blue']),  #type
            tick))  #born_tick


FPS = 60

pygame.init()
w, h = 800, 800
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

LKM = False
PKM = False

score = 0

AimBalls = []
level = 1
tick = 0

spawnAimBalls(5)
while True:
  xm, ym = pygame.mouse.get_pos()
  sc.fill('white')
  clock.tick(FPS)

  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      sys.exit()
    if ev.type == pygame.MOUSEBUTTONDOWN:
      if ev.button == 1:
        LKM = True
      if ev.button == 3:
        PKM = True
    if ev.type == pygame.MOUSEBUTTONUP:
      if ev.button == 1:
        LKM = False
      if ev.button == 3:
        PKM = False
  if tick % 300 == 0:
    level += 1
    spawnAimBalls(level)

  for ball in AimBalls:
    ball.draw()

  pygame.display.update()
  tick += 1
