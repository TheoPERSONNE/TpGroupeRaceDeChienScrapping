from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import breeds, recommendation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(breeds.router)
app.include_router(recommendation.router)
