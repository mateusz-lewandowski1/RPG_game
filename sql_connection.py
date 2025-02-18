from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from game import CharacterMenu

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'
    name = Column(String, primary_key=True)
    outfit = Column(Integer)
    character_kind = Column(String)
    kingdom = Column(String)
    mode = Column(String)

class Database:
    def __init__(self, db_url='sqlite:///main_db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

class CharacterManager:
    def __init__(self, db: Database):
        self.session = db.get_session()

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

    def display_characters(self):
        characters = self.session.query(Character).all()
        print("Characters in the database:")
        for character in characters:
            print(
                f'Name: {character.name}, Outfit: {character.outfit}, Kind: {character.character_kind}, Kingdom: {character.kingdom}, Mode: {character.mode}')

    def close(self):
        self.session.close()
