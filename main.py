import pygame
import sys

print("What should your picture be called?")
name = str(input())
print("What should be your draw Color? Red, Yellow, Blue, Green or White?")
colorInput = str(input())
if colorInput == "Red":
    color = (255, 0, 0)

if colorInput == "Yellow":
    color = (255, 255, 0)

if colorInput == "White":
    color = (255, 255, 255)
if colorInput == "Green":
    color = (0, 255, 0)
pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption('Finkel - ' + name)
clock = pygame.time.Clock()

radius = 10
Centre = pygame.mouse.get_pos()

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    press = pygame.key.get_pressed()
    # FarbenStart
    if press[pygame.K_c]:
        if press[pygame.K_b]:
            color = (0, 0, 255)
        if press[pygame.K_r]:
            color = (255, 0, 0)  #
        if press[pygame.K_y]:
            color = (255, 255, 0)
        if press[pygame.K_w]:
            color = (255, 255, 255)
    # Radius
    if press[pygame.K_t]:
        if press[pygame.K_UP]:
            radius += 1
        if press[pygame.K_DOWN]:
            radius -= 1
    # Wegradieren
    if press[pygame.K_x]:
        color = (0, 0, 0)
    # Eigene Farbe
    if press[pygame.K_j]:
        Red = int(input("Red-Value: "))
        Green = int(input("Green-Value: "))
        Blue = int(input("Blue-Value: "))
        CustomColor = (Red, Green, Blue)
    if press[pygame.K_m]:
        color = CustomColor
    # Welche Farbe?
    if press[pygame.K_k]:
        pygame.draw.circle(screen, color, (590, 590), 7)
    if press[pygame.K_l]:
        pygame.draw.circle(screen, (0, 0, 0), (590, 590), 7)
    # Schließen
    if press[pygame.K_ESCAPE]:
        sys.exit()
    # Malen
    if pygame.mouse.get_pressed() == (1, 0, 0):
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, (x, y), radius)
    # Speichern
    if press[pygame.K_s]:
        pygame.image.save(screen, "./Saves/" + name + ".png")
    pygame.display.update()
    clock.tick(100)
