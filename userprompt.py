import pygame
import constants as const

NO = 0
OK = 1

TITLE_SIZE = 40
TITLE_FONT = pygame.font.SysFont('Comic Sans MS', TITLE_SIZE)
TEXT_SIZE = 20
TEXT_FONT = pygame.font.SysFont('Comic Sans MS', TEXT_SIZE)

class UserPrompt():

    def __init__(self, title, msg, surface, position, size, max_chars = 16):
        """Create a blocking user prompt interface"""
        self.display_position = position
        self.display_screen = surface
        self.display_size = size
        self.msg = msg
        self.title = title
        self.result = None
        self.max_chars = max_chars
        #creates a buffer
        self.buffer = []
        #infinite loop
        self.prompt()

    def drawWindow(self):
        """Draw the window."""
        pygame.draw.rect(self.display_screen, (0,0,0), (*self.display_position, *self.display_size))
        pygame.draw.rect(self.display_screen, (255, 255, 255), (*self.display_position, *self.display_size), 2)

    def draw(self):
        """Draw the prompt window."""
        #draw the main window
        self.drawWindow()
        #buffer to string
        buffer = "".join(self.buffer)
        #create the title text
        title = TITLE_FONT.render(self.title, True, (255,255,255), (0,0,0))
        text = TEXT_FONT.render(self.msg + buffer, True, (255, 255, 255), (0, 0, 0))
        #with padding
        padx, pady = (10, 10)
        x, y = self.display_position
        self.display_screen.blit(title, (x + padx, y + pady))
        pygame.draw.rect(self.display_screen, (255, 255, 255), (x, y + pady + title.get_height(), self.display_size[0], self.display_size[1]), 2)
        y += title.get_height() + pady
        self.display_screen.blit(text, (x + padx, y + pady))

    def cancel(self):
        self.FLAG = NO

    def validate(self):
        self.result = "".join(self.buffer)
        self.FLAG = OK

    def buffer_add(self, arg):
        """Add a char to the buffer"""
        if len(self.buffer) <= self.max_chars:
            self.buffer.append(chr(arg))

    def buffer_remove(self):
        """Remove the last char of the buffer."""
        try:
            self.buffer.pop()
        except:
            pass

    def dispatchEvent(self):
        """Take all events and do actions with them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                #if it is a classical char
                if (event.key in list(range(pygame.K_a, pygame.K_z))) or event.key == pygame.K_SPACE:
                    self.buffer_add(event.key)
                #case of delete : remove the last char of the buffer
                if event.key == pygame.K_BACKSPACE:
                    self.buffer_remove()
                #if you enter retun key : return the buffer
                if event.key == pygame.K_RETURN:
                    self.validate()
                    return False
                #case of escape
                if event.key == pygame.K_ESCAPE:
                    self.cancel()
                    return False
        return True

    def prompt(self):
        """While 'return' isn't press, loop back."""
        flag = True
        while flag:
            flag = self.dispatchEvent()
            #draw
            self.draw()
            #update
            pygame.display.update()
        pygame.event.clear()


def askUser(title, msg, surface, position, size):
    m = UserPrompt(title, msg, surface, position, size)
    return m.FLAG, m.result
