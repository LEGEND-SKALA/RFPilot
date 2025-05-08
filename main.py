from fastapi import FastAPI
from dotenv import load_dotenv
from api.routers.router import router

load_dotenv()
app = FastAPI(title="RFPilot")

app.include_router(router)