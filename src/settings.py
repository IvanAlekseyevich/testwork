from environs import Env

env = Env()
env.read_env()


DATABASE_URL = env.str("DATABASE_URL")
ALLOWED_HOST: str = "localhost"
app_title: str = "Тестовое приложение"
app_description: str = "Сервис по расчёту стоимости страхования"


