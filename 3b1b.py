import pygame
import math


class Square(object):
    def __init__(self, size, xy, mass, speed):
        self.x = xy[0]
        self.y = xy[1]
        self.mass = mass
        self.v = speed
        self.size = size


width, height = 800, 400
white = pygame.Color('grey12')
gray = (200, 200, 200)
red = (200, 0, 0)

pygame.init()
background = pygame.display.set_mode((width, height))

SquareBig = Square(50, (320,200), math.pow(100, 5), -0.9/10000)
SquareSmall = Square(10, (100, 240), 1, 0)

count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for i in range(10000):

        if not(SquareSmall.x + SquareSmall.size < SquareBig.x or SquareSmall.x > SquareBig.x + SquareBig.size):
            count += 1

            sumM = SquareSmall.mass + SquareBig.mass
            v1 = (SquareSmall.mass - SquareBig.mass) / sumM * SquareSmall.v
            v1 += (2 * SquareBig.mass / sumM) * SquareBig.v

            sumM_ = SquareBig.mass + SquareSmall.mass
            v2 = (SquareBig.mass - SquareSmall.mass) / sumM_ * SquareBig.v
            v2 += (2 * SquareSmall.mass / sumM_) * SquareSmall.v

            SquareBig.v = v2
            SquareSmall.v = v1

        if SquareSmall.x <= 0:
            SquareSmall.v *= -1
            count += 1

        SquareBig.x += SquareBig.v
        SquareSmall.x += SquareSmall.v

    background.fill(white)
    pygame.draw.rect(background, (100, 100, 100), [0, 0, 800, 250])

    if SquareBig.x < 10:
        pygame.draw.rect(background, gray, [10, SquareBig.y, SquareBig.size, SquareBig.size])
        pygame.draw.rect(background, gray, [0, SquareSmall.y, SquareSmall.size, SquareSmall.size])
    else:
        pygame.draw.rect(background, gray, [SquareBig.x, SquareBig.y, SquareBig.size, SquareBig.size])
        pygame.draw.rect(background, gray, [SquareSmall.x, SquareSmall.y, SquareSmall.size, SquareSmall.size])

    font = pygame.font.SysFont(None, 50)
    text = font.render(str(count), True, (255, 255, 255))
    background.blit(text, [500, 50])
    pygame.display.update()
