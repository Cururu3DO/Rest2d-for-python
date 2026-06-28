import pygame
import importlib.util
import os
import sys
import time

# ==========================================================
# CARREGAR JOGO
# ==========================================================

if len(sys.argv) > 1:
    GAME_FILE = sys.argv[1]
else:
    GAME_FILE = "game.py"

spec = importlib.util.spec_from_file_location("game", GAME_FILE)
game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(game)

pygame.init()

WIDTH = getattr(game, "WIDTH", 800)
HEIGHT = getattr(game, "HEIGHT", 600)
TITLE = getattr(game, "TITLE", "REST Engine")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

# ==========================================================
# CACHE
# ==========================================================

_image_cache = {}

# ==========================================================
# GRAPHICS
# ==========================================================

class Graphics:

    def __init__(self):

        self._color = (255,255,255)

    def clear(self,r=0,g=0,b=0):

        screen.fill((r,g,b))

    def color(self,r,g,b):

        self._color = (r,g,b)

    def rectangle(self,mode,x,y,w,h):

        rect = pygame.Rect(x,y,w,h)

        if mode == "fill":

            pygame.draw.rect(
                screen,
                self._color,
                rect
            )

        else:

            pygame.draw.rect(
                screen,
                self._color,
                rect,
                1
            )

    def circle(self,mode,x,y,r):

        if mode == "fill":

            pygame.draw.circle(
                screen,
                self._color,
                (int(x),int(y)),
                int(r)
            )

        else:

            pygame.draw.circle(
                screen,
                self._color,
                (int(x),int(y)),
                int(r),
                1
            )

    def line(self,x1,y1,x2,y2):

        pygame.draw.line(
            screen,
            self._color,
            (x1,y1),
            (x2,y2)
        )

    def print(self,text,x,y,size=24):

        font = pygame.font.SysFont(
            None,
            size
        )

        img = font.render(
            str(text),
            True,
            self._color
        )

        screen.blit(
            img,
            (x,y)
        )

    def newImage(self,path):

        if not os.path.exists(path):

            path = os.path.join(
                "assets",
                path
            )

        if path in _image_cache:

            return _image_cache[path]

        image = pygame.image.load(
            path
        ).convert_alpha()

        _image_cache[path] = image

        return image

    def draw(self,image,x,y):

        screen.blit(
            image,
            (x,y)
        )

    def width(self):

        return screen.get_width()

    def height(self):

        return screen.get_height()

# ==========================================================
# KEYBOARD
# ==========================================================

class Keyboard:

    def isDown(self,key):

        keys = pygame.key.get_pressed()

        try:

            return keys[
                getattr(
                    pygame,
                    "K_"+key
                )
            ]

        except:

            return False

# ==========================================================
# MOUSE
# ==========================================================

class Mouse:

    def getPosition(self):

        return pygame.mouse.get_pos()

    def isDown(self,button=1):

        buttons = pygame.mouse.get_pressed()

        return buttons[button-1]

# ==========================================================
# TIMER
# ==========================================================

class Timer:

    def getTime(self):

        return time.time()

    def getFPS(self):

        return int(
            clock.get_fps()
        )

# ==========================================================
# REST
# ==========================================================

class Rest:

    def __init__(self):

        self.graphics = Graphics()

        self.keyboard = Keyboard()

        self.mouse = Mouse()

        self.timer = Timer()

rest = Rest()

game.rest = rest

# ==========================================================
# LOAD
# ==========================================================

if hasattr(game, "load"):
    game.load()

# ==========================================================
# LOOP PRINCIPAL
# ==========================================================

running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if hasattr(game, "keypressed"):

                game.keypressed(
                    pygame.key.name(event.key)
                )

        elif event.type == pygame.KEYUP:

            if hasattr(game, "keyreleased"):

                game.keyreleased(
                    pygame.key.name(event.key)
                )

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if hasattr(game, "mousepressed"):

                x, y = event.pos

                game.mousepressed(
                    x,
                    y,
                    event.button
                )

        elif event.type == pygame.MOUSEBUTTONUP:

            if hasattr(game, "mousereleased"):

                x, y = event.pos

                game.mousereleased(
                    x,
                    y,
                    event.button
                )

        elif event.type == pygame.MOUSEMOTION:

            if hasattr(game, "mousemoved"):

                x, y = event.pos

                dx, dy = event.rel

                game.mousemoved(
                    x,
                    y,
                    dx,
                    dy
                )

    if hasattr(game, "update"):
        game.update(dt)

    if hasattr(game, "draw"):
        game.draw()

    pygame.display.flip()

pygame.quit()