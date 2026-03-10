import sqlite3
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import sys
'''
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

cursor . execute (
" SELECT name FROM users WHERE User_type = ? " ,
("Md",)
)

for ligne in cursor . fetchall () :
    print ( ligne )
conn . close ()
'''


class App():
    def __init__(self):
        pygame.init()
        self.window_height = 600
        self.window_width = 800
        self.window_size = self.window_width, self.window_height
        self.Manager = pygame_gui.UIManager(self.window_size)
        self.window_surface = pygame.display.set_mode((self.window_size)) 

    def Event_Process(self,event):
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            pass

    def run(self):
        Framerate = 60 
        clock = pygame.time.Clock()

        while True:
            time_delta = clock.tick(Framerate)

            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    sys.exit()
                if not self.Manager.process_events(event):
                        self.Event_Process(event)

            self.Manager.update(time_delta/1000)
            pygame.draw.rect(self.window_surface, (30, 30, 30), pygame.Rect((0, 0), self.window_size))
            self.Manager.draw_ui(self.window_surface)
            pygame.display.flip()

App().run()