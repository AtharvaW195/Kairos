from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router

app = FastAPI(title="Kairos API")

# The local React development server runs on a separate origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://kairos-nu-plum.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
