from fastapi import FastAPI
from .controllers.math_controller import router as math_router
from .models.db_session import init_db

app = FastAPI(title="Math Microservice")
app.include_router(math_router)
init_db()
