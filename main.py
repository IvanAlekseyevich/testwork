import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.routers import router_calculate, router_rate
from src.settings import settings

# app = FastAPI(debug=True)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[settings.ALLOWED_HOST, 'http://localhost:3000', 'http://localhost'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )




app = FastAPI(title=settings.app_title, description=settings.app_description, debug=True)
app.include_router(router_calculate)
app.include_router(router_rate)

# if __name__ == "__main__":
#     uvicorn.run(
#         app,
#         host="0.0.0.0",
#         port=8001,
#         log_level="info",
#         reload=False,
#     )
