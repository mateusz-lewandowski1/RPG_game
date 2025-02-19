from game import CharacterMenu, World, ValidationError, Player
from sql_connection import CharacterManager, Database

class Game:
    def __init__(self):
        self.chosen_character = None
        self.player = None

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

        db = Database()
        self.player = Player(self.chosen_character)
        character_manager = CharacterManager(db, self.chosen_character, self.player)

        character_manager.add_character(self.chosen_character)

        character_manager.add_item("Mystic Bow")
        character_manager.add_item("Mana Potion")

        character_manager.display_characters()

        character_manager.close()

        #world.map_m1()

if __name__ == '__main__':
    game = Game()
    game.main()
