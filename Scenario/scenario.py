import pygame

class Scenario:
    def __init__(self, state_machine):
        self._white = (255, 255, 255)
        self._state_machine = state_machine

    def display_backgroud(self):
        pass

    def handle_event(self, event):
        pass


class StartupScenario(Scenario):
    def __init__(self, state_machine):
        Scenario.__init__(self, state_machine)
        self._screen_size = (533, 300)
        self._firstpage = pygame.image.load(r"Resource\Images\Background\firstpage.jpg")

    def display_backgroud(self):
        self._startup_screen = pygame.display.set_mode(self._screen_size)
        self._startup_screen.fill(self._white)
        self._startup_screen.blit(self._firstpage, (0, 0))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._state_machine.change_scenario('menu')
            self._state_machine.run()


class MenuScenario(Scenario):
    def __init__(self, state_machine):
        Scenario.__init__(self, state_machine)
        self._screen_size = (900, 600)
        self.load_resource()

    def load_resource(self):
        self.main_background = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\main_background.png")
        self.select10 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select10.png")
        self.select11 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select11.png")
        self.select20 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select20.png")
        self.select21 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select21.png")
        self.select30 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select30.png")
        self.select31 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select31.png")
        self.select40 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select40.png")
        self.select41 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\select41.png")
        self.player_screen = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\PlayerScreen.png")
        self.change_player0 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\changePlayer1.png")
        self.change_player1 = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\changePlayer2.png")
        print (self.change_player0.get_width(), self.change_player0.get_height())
        self.ps = pygame.image.load(r"Resource\Images\Items\MainMenu.atlas\ps.png")
        self.change_player_position = (0, 140)
        self.select1_position = (520, 100)
        self.select2_position = (520, 180)
        self.select3_position = (520, 260)
        self.select4_position = (520, 340)
        self.change_player_width, self.change_player_height = (290, 70)
        self.select_width, self.select_height = (150, 70)
        self.menu_map = {
            'change_player0' : self.change_player0,
            'change_player1' : self.change_player1,
            'select10' : self.select10,
            'select11' : self.select11,
            'select20' : self.select20,
            'select21' : self.select21,
            'select30' : self.select30,
            'select31' : self.select31,
            'select40' : self.select40,
            'select41' : self.select41,
        }
        self.menu_status = {
            'change_player' : '0',
            'select1' : '1',
            'select2' : '0',
            'select3' : '0',
            'select4' : '0',
        }
        self.menu_position = {
            'change_player' : self.change_player_position,
            'select1' : self.select1_position,
            'select2' : self.select2_position,
            'select3' : self.select3_position,
            'select4' : self.select4_position,
        }
        self.menus = ('change_player', 'select1', 'select2', 'select3', 'select4')

    def display_changed_menu(self, menus):
        self.menu_screen.fill(self._white)
        for menu in menus:
            self.main_background.blit(self.menu_map[menu], self.menu_position[menu[:-1]])
        self.menu_screen.blit(self.main_background, (0, 0))
        pygame.display.flip()

    def get_changed_menus(self, mouse_position, curr_menus):
        mouse_x, mouse_y = mouse_position
        print ("Position: ", mouse_position)
        changed_menus = []
        for menu in curr_menus:
            menu_surface = self.menu_map[menu]
            height, width= menu_surface.get_height(), menu_surface.get_width()
            menu_x, menu_y = self.menu_position[menu[:-1]][0], self.menu_position[menu[:-1]][1]
            if mouse_x >= menu_x and mouse_x < menu_x + width \
                and mouse_y >= menu_y and mouse_y < menu_y + height:
                changed_status = '0' if menu[-1] == '1' else '1'
                menu = menu[:-1] + changed_status
                self.menu_status[menu[:-1]] = changed_status
            changed_menus.append(menu)
        return changed_menus

    def handle_click_menu(self, event):
        curr_menus = []
        for key, value in self.menu_status.items():
            curr_menus.append(key+value)
        changed_menus = self.get_changed_menus(event.pos, curr_menus)
        print ("changed_menus: ", changed_menus)
        self.display_changed_menu(changed_menus)

    def display_backgroud(self):
        self.menu_screen = pygame.display.set_mode(self._screen_size)
        self.menu_screen.fill(self._white)
        self.main_background.blit(self.player_screen, (0, 0))
        self.main_background.blit(self.change_player1, (0, 140))
        self.main_background.blit(self.ps, (0, 190))
        self.main_background.blit(self.select11, self.select1_position)
        self.main_background.blit(self.select20, self.select2_position)
        self.main_background.blit(self.select30, self.select3_position)
        self.main_background.blit(self.select40, self.select4_position)
        self.menu_screen.blit(self.main_background, (0, 0))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_click_menu(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.handle_click_menu(event)


class SecnarioStateMachine:
    def __init__(self):
        self._scenario_map = {}
        self._current_scenario = None

    def add_scenario(self, name, scenario):
        name = name.upper()
        self._scenario_map[name] = scenario

    def change_scenario(self, name):
        name = name.upper()
        self._current_scenario = self._scenario_map[name]

    def run(self):
        self._current_scenario.display_backgroud()

    def get_current_scenario(self):
        return self._current_scenario
