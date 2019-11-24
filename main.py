import pygame
#init pygame
pygame.init()
pygame.font.init()

import blocks
import games
import constants as const
import sys
import random
import userprompt

const.FONT = pygame.font.SysFont('Comic Sans MS', 30)
const.WINDOW_INFOS = pygame.display.Info()
const.WINDOW_SIZE = (const.WINDOW_INFOS.current_w, const.WINDOW_INFOS.current_h)
const.WINDOW = pygame.display.set_mode(const.WINDOW_SIZE, pygame.FULLSCREEN)
DISPLAY_SURFACE = pygame.display.get_surface()
FPS_CLOCK = pygame.time.Clock()

class Main():

    def __init__(self):
        self._in_game = True
        userprompt.askUser("Game", """I hope you'll enjoy my game ! \
Press 'enter' to start playing !""",
                           DISPLAY_SURFACE, (0,0), const.WINDOW_SIZE)
        self.changeMap(games.chooseRandomMap())

    def changeMap(self, _map):
        _map.resetDefault()
        self._actual_map = _map
        const.WINDOW.fill((0, 0, 0))

    def quit(self):
        pygame.quit()
        sys.exit(0)

    def dispatchEvents(self):
        """Takes all events and do something with them."""
        mouse_event = pygame.mouse
        key_states = pygame.key.get_pressed()
        #keyboard
        if key_states[pygame.K_ESCAPE]:
            self.quit()
        if key_states[pygame.K_w] or key_states[pygame.K_UP]:
            self._actual_map.move(const.UP)
        if key_states[pygame.K_s] or key_states[pygame.K_DOWN]:
            self._actual_map.move(const.DOWN)
        if key_states[pygame.K_d] or key_states[pygame.K_RIGHT]:
            self._actual_map.move(const.RIGHT)
        if key_states[pygame.K_a] or key_states[pygame.K_LEFT]:
            self._actual_map.move(const.LEFT)
        # link and player
        onlink = self._actual_map.onLink()
        if onlink is not None and not self._actual_map.wasOnLink():
            #check the path
            for i, _map in enumerate(games.AVAIBLE_MAPS):
                if _map._map_path != onlink:
                    continue
                #ask the user
                yes, p = userprompt.askUser("Link", "Continue ? (y / n) : ", DISPLAY_SURFACE, (50,50), (500,500))
                if yes == userprompt.OK and p == "y":
                    self._actual_map.resetDefault()
                    #if found, change map
                    self.changeMap(games.AVAIBLE_MAPS[i])
                else:
                    pass
        #event loop
        for event in pygame.event.get():
            #if quit button triggered, quit
            if event.type == pygame.QUIT:
                self._in_game = False
                self.quit()

    def run(self):
        while self._in_game:
            #get the pygame events
            self.dispatchEvents()
            #redraw
            self._actual_map.display(DISPLAY_SURFACE)
            FPS_CLOCK.tick(const.FPS)
            #update
            pygame.display.update()

if __name__ == "__main__":
    app = Main()
    app.run()
