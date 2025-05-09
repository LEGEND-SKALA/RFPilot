from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from api.routers.router import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="RFPilot")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your Vue frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)