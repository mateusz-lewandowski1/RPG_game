from game import CharacterMenu
from game import World
from game import ValidationError

class Game:
    def __init__(self):
        self.chosen_character = None

    def main(self):
        input_name = input("Enter your character name:\n")
        input_outfit = int(input("Choose your outfit (1 or 2):\n"))
        input_character_kind = input("Choose your character's kind ('Warrior', 'Sura', 'Ninja', 'Shaman'):\n")
        input_kingdom = input("Choose your kingdom ('Chunjo', 'Jinno', 'Shinsoo'):\n")
        input_mode = input("Choose your mode (singleplayer, multiplayer):\n")

        try:
            self.chosen_character = CharacterMenu(input_name, mode=input_mode, outfit=input_outfit, character_kind=input_character_kind, kingdom=input_kingdom)
            print(self.chosen_character)
        except ValidationError as e:
            print(e)
            return

        CharacterMenu.screen_loading()

        world = World(self.chosen_character)

        world.welcome_message()
        world.map_m1()

if __name__ == '__main__':
    game = Game()  # No arguments needed
    game.main()
