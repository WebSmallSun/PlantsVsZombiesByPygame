import sys
import pygame
from Scenario.scenario import StartupScenario, MenuScenario, SecnarioStateMachine

class MyGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("植物大战僵尸")
        self._state_machine = SecnarioStateMachine()
        self._state_machine.add_scenario('startup', StartupScenario(self._state_machine))
        self._state_machine.add_scenario('menu', MenuScenario(self._state_machine))

    def run(self):
        self._state_machine.change_scenario('startup')
        self._state_machine.run()
        while True:
            for event in pygame.event.get():
                current_scenario = self._state_machine.get_current_scenario()
                current_scenario.handle_event(event)

if __name__ == "__main__":
    my_game = MyGame()
    my_game.run()