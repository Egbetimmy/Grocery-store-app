import mysql.connector
import os
from dotenv import load_dotenv

# Load the .env file into environment variables
load_dotenv()

# Access environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

__cnx = None


def get_sql_connection():
    print("Opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
            user=db_user,
            password=db_password,
            database=db_name
        )

    return __cnx

