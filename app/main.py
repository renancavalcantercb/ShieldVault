from fastapi import FastAPI
from app.api.v1.endpoints import auth, passwords
from app.db.session import engine
from app.db.models import Base

app = FastAPI()

app.include_router(auth.router)
app.include_router(passwords.router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
