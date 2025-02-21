from pydantic import BaseModel, ValidationError, conint
from typing import Literal
import time

class CharacterSpecs(BaseModel):
    character_kind: Literal['Warrior', 'Sura', 'Ninja', 'Shaman']
    outfit: conint(ge=1, le=2)
    name: str
    kingdom: Literal['Chunjo', 'Jinno', 'Shinsoo']
    mode: Literal['singleplayer', 'multiplayer']

class CharacterMenu(CharacterSpecs):
    def __init__(self, name: str, /, mode: str, outfit: int = 1, character_kind: str = 'Warrior', kingdom: str = 'Chunjo'):
        params = {
            'name': name,
            'outfit': outfit,
            'character_kind': character_kind,
            'kingdom': kingdom,
            'mode': mode
        }
        super().__init__(**params)  # This will validate outfit and other fields

        self._specs = params  # Use a private variable to avoid Pydantic validation issues

    @property
    def specs(self):
        return self._specs  # Provide access to the specs

    @staticmethod
    def screen_loading():
        print('Loading', end='', flush=True)
        for i in range(3):
            time.sleep(1)
            print('.', end='', flush=True)
        print('\nLoading complete')

class World:
    def __init__(self, character_menu: CharacterMenu):
        self.character_menu = character_menu
        self.items = None

    def welcome_message(self):
        if self.character_menu.kingdom == 'Chunjo':
            print('Welcome to Chunjo! Explore the world.')
        elif self.character_menu.kingdom == 'Jinno':
            print('Welcome to Jinno! Explore the world.')
        elif self.character_menu.kingdom == 'Shinsoo':
            print('Welcome to Shinsoo! Explore the world.')
        else:
            print('Loading error. Please choose the correct kingdom available.')

    def map_m1(self):
        self.items = []
        try:
            with open('items.txt', 'r') as file:
                self.items = [line.strip() for line in file.readlines()]

            print("Items in the map:")
            for item in self.items:
                print(f"- {item}")

        except FileNotFoundError:
            print("items.txt file not found!")


class Player:
    def __init__(self, character_menu: CharacterMenu):
        self.chosen_character = character_menu
        self.level = 1
        self.health = 100
        self.mana = 100
        self.skills = None
        self.inventory = []
        self.item = None
        self.position = (0, 0)

class Actions(Player):
    def __init__(self, character_menu: CharacterMenu):
        super().__init__(character_menu)

    def move(self, direction):
        if direction == 'left':
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == 'right':
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 'up':
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 'down':
            self.position = (self.position[0], self.position[1] + 1)
        else:
            print('Invalid direction. Please choose the correct direction.')

    def pick_item(self):
        self.inventory.append(self.item)
        print(f"Picked up {self.item}!")
