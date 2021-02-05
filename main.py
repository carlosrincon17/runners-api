import pathlib

import i18n
import uvicorn
from fastapi import FastAPI, Request, Response

from database import SessionLocal
from routers import auth, user

app = FastAPI()

current_dir = pathlib.Path(__file__).parent
i18n.load_path.append("{}/translations/".format(current_dir))
i18n.set('locale', 'es')


@app.get("/")
async def root():
    return {"message": "Runners API v1.0"}


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["Users"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)