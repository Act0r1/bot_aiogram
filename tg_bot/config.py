from dataclasses import dataclass
from typing import List
from environs import Env


@dataclass
class Bot:
    token: str
    admins: List[int]


@dataclass
class Database:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Config:
    tg_bot: Bot
    db: Database


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=Bot(
            token=env.str("API_TOKEN"), admins=list(map(int, env.list("ADMINS")))
        ),
        db=Database(
            host=env.str("DB_HOST"),
            password=env.str("DB_PASSWORD"),
            user=env.str("DB_USER"),
            database=env.str("DB_NAME"),
        ),
    )
