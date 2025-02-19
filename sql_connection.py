from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from game import CharacterMenu, Actions, Player

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    name = Column(String, primary_key=True)
    outfit = Column(Integer)
    character_kind = Column(String)
    kingdom = Column(String)
    mode = Column(String)
    inventory = Column(String)

class Database:
    def __init__(self, db_url='sqlite:///main_db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

class CharacterManager:
    def __init__(self, db: Database, character_menu: CharacterMenu, player_inventory: Player):
        self.session = db.get_session()
        self.action = Actions(character_menu)
        self.player_inventory = player_inventory.inventory
        self.item = player_inventory.item

    def add_character(self, character_menu: CharacterMenu):
        new_character = Character(
            name=character_menu.name,
            outfit=character_menu.outfit,
            character_kind=character_menu.character_kind,
            kingdom=character_menu.kingdom,
            mode=character_menu.mode
        )

        self.session.add(new_character)
        self.session.commit()
        print(f'Added character: {new_character.name}')

    def add_item(self, item):
        self.item = item

        character = self.session.query(Character).filter_by(name=self.action.chosen_character.name).first()

        if character:
            if character.inventory is None:
                character.inventory = ""

            if character.inventory:
                character.inventory += f", {self.item}"
            else:
                character.inventory = self.item

            self.session.commit()
            print(f'Added item: {self.item} to {character.name}\'s inventory.')
        else:
            print(f'Character not found in the database.')


    def display_characters(self):
        characters = self.session.query(Character).all()
        print("Characters in the database:")
        for character in characters:
            print(
                f'Name: {character.name}, Outfit: {character.outfit}, Kind: {character.character_kind}, Kingdom: {character.kingdom}, Mode: {character.mode}')

    def delete_character(self, character_menu: CharacterMenu):
        character_to_delete = self.session.query(Character).filter_by(name=character_menu.name).first()

        if character_to_delete:
            self.session.delete(character_to_delete)
            self.session.commit()
            print(f'Deleted character: {character_menu.name}')
        else:
            print(f'Character "{character_menu.name}" not found in the database.')


    def close(self):
        self.session.close()
