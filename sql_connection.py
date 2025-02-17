from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = 'your_username'
password = 'your_password'
host = 'localhost'  # or your database host
port = '5432'       # default port for PostgreSQL
database = 'your_database'

database_url = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)

session = Session()

# Example
try:
    result = session.execute("SELECT * FROM your_table")
    for row in result:
        print(row)
finally:
    # Close the session
    session.close()
