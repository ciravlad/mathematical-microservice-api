from fastapi import FastAPI
from .controllers.math_controller import router as math_router

app = FastAPI(title="Math Microservice")
app.include_router(math_router)