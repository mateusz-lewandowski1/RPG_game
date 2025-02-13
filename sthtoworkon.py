class Game:
    def __init__(self):
        self.character_menu = None
        self.world = None

    def create_character(self):
        input_name = input("Enter your character name:\n")
        input_outfit = int(input("Choose your outfit (1 or 2):\n"))
        input_character_kind = input("Choose your character's kind ('Warrior', 'Sura', 'Ninja', 'Shaman'):\n")
        input_kingdom = input("Choose your kingdom ('Chunjo', 'Jinno', 'Shinsoo'):\n")
        input_mode = input("Choose your mode (singleplayer, multiplayer):\n")

        try:
            self.character_menu = CharacterMenu(input_name, mode=input_mode, outfit=input_outfit, character_kind=input_character_kind, kingdom=input_kingdom)
            print(self.character_menu)
        except ValidationError as e:
            print(e)
            return  # Exit if validation fails

    def start(self):
        self.create_character()
        CharacterMenu.screen_loading()

        # Create an instance of the World class
        self.world = World(self.character_menu)

        # Call the welcome_message method
        self.world.welcome_message()

        # Call the map_m1 method
        self.world.map_m1()

if __name__ == '__main__':
    game = Game()
    game.start()

###### COS ZMIENIC TO JAKOS NA ROZNE MODULY I LOGIKA Z MAINEM PRZEROBIC
