import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+pymysql://root:linux@localhost:3306/flask_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv(
        "SECRET_KEY", "ad0f870484d99257f7fe75892eb22b1ac2a6ba71ffb205eba2a32ba58f99a09b"
    )
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "ca102cfe36190079543b63d9c8d0b4f51eda0e950d480cc5e73d785b98cdcd12",
    )
    JWT_ALGORITHM = "HS256"
