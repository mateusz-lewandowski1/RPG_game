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
        super().__init__(**params)  # This will validate all fields
        # Store specs as a private instance variable
        self._specs = params  # Private variable to avoid Pydantic validation issues

    @property
    def specs(self):
        return self._specs  # Access to the specs

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

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"Picked up {item}!")

def main():
    input_name = input("Enter your character name:\n")
    input_outfit = int(input("Choose your outfit (1 or 2):\n"))
    input_character_kind = input("Choose your character's kind ('Warrior', 'Sura', 'Ninja', 'Shaman'):\n")
    input_kingdom = input("Choose your kingdom ('Chunjo', 'Jinno', 'Shinsoo'):\n")
    input_mode = input("Choose your mode (singleplayer, multiplayer):\n")

    try:
        chosen_character = CharacterMenu(input_name, mode=input_mode, outfit=input_outfit, character_kind=input_character_kind, kingdom=input_kingdom)
        print(chosen_character)
    except ValidationError as e:
        print(e)
        return

    CharacterMenu.screen_loading()

    world = World(chosen_character)

    world.welcome_message()

    world.map_m1()

if __name__ == '__main__':
    main()




