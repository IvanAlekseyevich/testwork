from environs import Env

env = Env()
env.read_env()

DATABASE_URL = env.str("DATABASE_URL")
ALLOWED_HOST = env.str("ALLOWED_HOST")
APP_TITLE = env.str("APP_TITLE")
APP_DESCRIPTION = env.str("APP_DESCRIPTION")
