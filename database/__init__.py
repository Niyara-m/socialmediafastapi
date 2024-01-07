from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Ссылка к базе данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

# Подключение к Базе
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Общий класс для наследования в models
Base = declarative_base()

# Генератор сессий к базе
session = sessionmaker(bind=engine)

# Генератор подключений к базе
from .models import User

def get_db():
    db = session()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()