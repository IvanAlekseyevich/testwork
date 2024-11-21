from fastapi import FastAPI

from src import settings
from src.api.routers import router_calculate, router_rate


app = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION, debug=True)
app.include_router(router_calculate)
app.include_router(router_rate)
