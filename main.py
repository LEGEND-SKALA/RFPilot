from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from api.routers.router import router
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="RFPilot")

app.include_router(router)