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

    active_user_name = None
    active_user_password = None
    active_user_id = None
    active_user_type = None
    
    active_window = 'main_interface'
    need_to_update_interface = False

    def __init__(self):
        pygame.init()
        self.window_height = 600
        self.window_width = 800
        self.window_size = self.window_width, self.window_height
        self.Manager = pygame_gui.UIManager(self.window_size)
        self.window_surface = pygame.display.set_mode((self.window_size)) 

    def connect_db(self,database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def assign_widget_position(self, widget_size, x_rel_pos, y_rel_pos):
        window_height = self.window_height
        window_width = self.window_width
        x_pos = x_rel_pos * window_width - (widget_size[0] / 2)
        y_pos = y_rel_pos * window_height - (widget_size[1] / 2)
        return (x_pos, y_pos)
    
    def interface_clear(self):
        for sprite in self.Manager.ui_group._spritelist[1:len(self.Manager.ui_group._spritelist)]:
            if sprite.text != self.back_button_text:
                sprite.kill()

    def build_main_interface(self):

        button_size = 200,50
        login_button_text = "Login"
        register_button_text = "Register"

        login_button_rel_pos = self.assign_widget_position(button_size, 0.35, 0.5)
        register_button_rel_pos = self.assign_widget_position(button_size, 0.65, 0.5)

        login_button = UIButton(relative_rect=pygame.Rect(login_button_rel_pos, button_size), text= login_button_text, manager=self.Manager)
        register_button = UIButton(relative_rect=pygame.Rect(register_button_rel_pos, button_size), text= register_button_text, manager=self.Manager)

    def build_login_interface(self):

        label_size = 200,50
        login_button_size = 100,50
        text_entry_size = 200,50

        user_label_text = "Please login to your account"
        login_button_text = "Login"
        username_entry_placeholder = "Enter your username"
        password_entry_placeholder = "Enter your password"

        user_label_rel_pos = self.assign_widget_position(label_size, 0.5, 0.20)
        username_entry_rel_pos = self.assign_widget_position(text_entry_size, 0.5, 0.3)
        password_entry_rel_pos = self.assign_widget_position(text_entry_size, 0.5, 0.4)
        login_button_rel_pos = self.assign_widget_position(login_button_size, 0.5, 0.5)

        label = UILabel(relative_rect=pygame.Rect(user_label_rel_pos, label_size), text= user_label_text, manager=self.Manager)
        username_entry = UITextEntryLine(relative_rect=pygame.Rect(username_entry_rel_pos, text_entry_size),placeholder_text= username_entry_placeholder, manager=self.Manager)
        password_entry = UITextEntryLine(relative_rect=pygame.Rect(password_entry_rel_pos, text_entry_size),placeholder_text= password_entry_placeholder, manager=self.Manager)
        button = UIButton(relative_rect=pygame.Rect(login_button_rel_pos, login_button_size), text= login_button_text, manager=self.Manager)

    def build_register_interface(self):

        label_size = 200,50
        login_button_size = 100,50
        text_entry_size = 200,50

        user_label_text = "Create your account"
        login_button_text = "Register"
        username_entry_placeholder = "Enter your username"
        password_entry_placeholder = "Enter your password"
        confirm_password_entry_placeholder = "Confirm your password"

        user_label_rel_pos = self.assign_widget_position(label_size, 0.5, 0.20)
        username_entry_rel_pos = self.assign_widget_position(text_entry_size, 0.5, 0.3)
        password_entry_rel_pos = self.assign_widget_position(text_entry_size, 0.5, 0.4)
        confirm_password_entry_rel_pos = self.assign_widget_position(text_entry_size, 0.5, 0.5)
        login_button_rel_pos = self.assign_widget_position(login_button_size, 0.5, 0.6)

        label = UILabel(relative_rect=pygame.Rect(user_label_rel_pos, label_size), text= user_label_text, manager=self.Manager)
        username_entry = UITextEntryLine(relative_rect=pygame.Rect(username_entry_rel_pos, text_entry_size),placeholder_text= username_entry_placeholder, manager=self.Manager)
        password_entry = UITextEntryLine(relative_rect=pygame.Rect(password_entry_rel_pos, text_entry_size),placeholder_text= password_entry_placeholder, manager=self.Manager)
        confirm_password_entry = UITextEntryLine(relative_rect=pygame.Rect(confirm_password_entry_rel_pos, text_entry_size),placeholder_text= confirm_password_entry_placeholder, manager=self.Manager)
        button = UIButton(relative_rect=pygame.Rect(login_button_rel_pos, login_button_size), text= login_button_text, manager=self.Manager)
    
    def build_back_button(self):
        button_size = 100,50
        self.back_button_text = "Back"
        back_button_rel_pos = self.assign_widget_position(button_size, 0.9, 0.9)
        back_button = UIButton(relative_rect=pygame.Rect(back_button_rel_pos, button_size), text= self.back_button_text, manager=self.Manager)
    
    def window_interface_update(self):
        self.interface_clear()

        print('building:',self.active_window)

        if self.active_window == 'main_interface':
            self.build_main_interface()
        if self.active_window == 'login_interface':
            self.build_login_interface()
        if self.active_window == 'register_interface':
            self.build_register_interface()
        
        self.need_to_update_interface = False
        
    def going_back(self):
        self.need_to_update_interface = True
        if self.active_window == 'main_interface':
            pass
        if self.active_window == 'login_interface':
            self.active_window = 'main_interface'
        if self.active_window == 'register_interface':
            self.active_window = 'main_interface'    

    def register_account(self, username, password):
        self.connect_db("Database.db")
        self.cursor.execute("INSERT INTO User (Name, Hashed_Password) VALUES (?,?)",(username,password))
        self.conn.commit ()

    def check_user_credentials(self, username, password):
        pass

    def event_process(self,event):
        if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            pass
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            
            
            if event.ui_element.text == "Login":
                self.active_window = 'login_interface'
                self.need_to_update_interface = True
            if event.ui_element.text == "Register":
                self.active_window = 'register_interface'
                self.need_to_update_interface = True

            if event.ui_element.text == self.back_button_text:
                self.going_back()

    def run(self):
        Framerate = 60 
        clock = pygame.time.Clock()
        self.build_main_interface()
        self.build_back_button()
        self.register_account('un_test','pw_test')
        while True:
            time_delta = clock.tick(Framerate)

            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    sys.exit()
                if not self.Manager.process_events(event):
                        self.event_process(event)
            
            if self.need_to_update_interface:
                self.window_interface_update()

            self.Manager.update(time_delta/1000)
            pygame.draw.rect(self.window_surface, (30, 30, 30), pygame.Rect((0, 0), self.window_size))
            self.Manager.draw_ui(self.window_surface)
            pygame.display.flip()

App().run()