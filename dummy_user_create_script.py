import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from passlib.hash import sha256_crypt

engine = create_engine('sqlite:///pomodoro_data.db', echo=True)

#სესიის შექმნა
Session = sessionmaker(bind = engine)
session = Session()


user = User('admin', sha256_crypt.hash('password'))
session.add(user)

user = User('namper33', sha256_crypt.hash('tits'))
session.add(user)

user = User('user', sha256_crypt.hash('user'))
session.add(user)

session.commit()