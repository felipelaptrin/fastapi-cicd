import os
from dotenv import load_dotenv
from peewee import MySQLDatabase


load_dotenv()

db = MySQLDatabase(
    os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT")),
)
