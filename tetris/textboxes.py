from random import randint
import pygame
import utils


pygame.init()
pygame.font.init()
pygame.mixer.init()

couriernewBig = pygame.font.SysFont('couriernew', 38)
couriernewBigBold = pygame.font.SysFont('couriernew', 38, bold=True)
couriernewSmall = pygame.font.SysFont('couriernew', 25)
couriernewScore = pygame.font.SysFont('couriernew', 60)


class Text:
    def __init__(self, screen: pygame.Surface, color: tuple, coords: utils.Coordinates, font: pygame.font.Font, text: str = ""):
        self._text = text
        self._screen = screen
        self._color = color
        self._coords = coords
        self._font = font

    def updateText(self, newText: str):
        self._text = newText

    def getText(self):
        return self._text

    def draw(self):
        self._screen.blit(self._font.render(self._text, False, self._color), (self._coords.x, self._coords.y))

class Time(Text):
    def __init__(self, screen: pygame.Surface, coords: utils.Coordinates, startTime: float = 0.0):
        super().__init__(screen, (88, 88, 88), coords, couriernewSmall, "")
        self._milliseconds = startTime

    def tick(self, difference: float):
        self._milliseconds += difference
        super().updateText(utils.formatMilliseconds(self._milliseconds))

    def draw(self):
        self._screen.blit(self._font.render(self._text, False, self._color), (self._coords.x + 80, self._coords.y))
        self._screen.blit(self._font.render("Time:", False, (150, 150, 150)), (self._coords.x, self._coords.y))

# A2.2 use modular design concepts that support reusable code (e.g., encapsulation, inheritance, method overloading, method overriding, polymorphism);
# inheritance, method overriding within the inheritance

# C1.1 decompose a problem into modules, classes, or abstract data types (e.g., stack, queue, dictionary) using an object-oriented design methodology (e.g., CRC [Class Responsibility Collaborator] or UML [Unified Modeling Language]);

# -------- testing ---------
size = (1200, 900)
screen = pygame.display.set_mode(size)

def main():
    t = Text(screen, (100, 100, 100), utils.Coordinates(50, 50), couriernewBig, "wasd")
    time = Time(screen, utils.Coordinates(200, 200))
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        t.draw()
        time.tick(100/6)
        time.draw()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()