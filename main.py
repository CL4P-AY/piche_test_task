from fastapi import FastAPI, Request

from middlewares.rate_limiter import add_rate_limiter, limiter
from routers import accounts, users
from settings import RATE_LIMIT, APP_TITLE

app = FastAPI(title=APP_TITLE)
add_rate_limiter(app)


@app.middleware("http")
def rate_limiter_middleware(request: Request, call_next):
    @limiter.limit(RATE_LIMIT)
    def wrapper(request: Request):
        return call_next(request)

    return wrapper(request)


app.include_router(accounts.router)
app.include_router(users.router)
