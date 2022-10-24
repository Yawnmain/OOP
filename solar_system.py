import pygame
import math
pygame.init()

# Параметры окна
WIDTH = 1200
HEIGHT = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar system")

# Цвета планет
SUN = (255, 255, 0)
EARTH = (65, 105, 225)
MERC = (80, 78, 81)
VENUS = (135, 68, 25)
MARS = (193, 165, 139)
JUPYTER = (255, 0, 0)
SAT = (224, 207, 143)
UR = (130, 163, 181)
NEP = (41, 65, 98)


class Planet:

    def __init__(self, x, y, radius, color, radius_tr, angle, tick):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius  # Радиус планеты
        self.radius_tr = radius_tr  # Радиус траектории
        self.angle = angle
        self.orbit = []
        self.tick = tick

    def draw(self, win):  # Отрисовка планет и их орбит
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    # Реализация движения планет
    def new_coords(self):
        M = math.radians(self.angle)
        self.x = self.x + self.radius_tr * math.cos(M)
        self.y = self.y + self.radius_tr * math.sin(M)
        return self.x, self.y

    def move(self, planets):
        self.tick += 1
        self.angle += 1
        self.x, self.y = self.new_coords()
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()
    # Для расположения использовалось относильеное позиционирование
    sun = Planet(600, 450, 30, SUN, 0, 0, 0)

    mercury = Planet(600, 340, 4, MERC, 2, 0, 0)

    venus = Planet(600, 625, 8, VENUS, -3, 0, 0)

    earth = Planet(825, 415, 10, EARTH, 4, -280, 0)

    mars = Planet(500, 720, 5, MARS, -5, 20, 0)

    jupyter = Planet(600, 110, 20, JUPYTER, 6, 0, 0)

    saturn = Planet(200, 450, 17, SAT, -7, 90, 0)

    uran = Planet(230, 190, 15, UR, -8, 125, 0)

    neptun = Planet(930, 850, 16, NEP, -9, 320, 0)

    planets = [sun, mercury, venus, earth, mars, jupyter, saturn, uran, neptun]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.move(planets)
            planet.draw(WIN)

        pygame.display.update()


main()
