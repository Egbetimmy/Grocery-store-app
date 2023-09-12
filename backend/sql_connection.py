import mysql.connector

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(user='Timmy', password='tanrose1996', database='grocery_app')

    return __cnx


'''
from sqlalchemy import create_engine

engine = None

def get_sql_connection():
    global engine
    
    if engine is None:
        engine = create_engine('mysql+mysqlconnector://root:tanrose1996@localhost/grocery_app', echo=True)

    return engine.connect()

'''
