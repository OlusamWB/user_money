from fastapi import FastAPI

from routes.user import user_router
from routes.account import account_router
from routes.transaction import transaction_router
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.include_router(user_router, tags=["user"])
app.include_router(account_router, prefix="/accounts", tags=["account"])
app.include_router(transaction_router, prefix="/transactions", tags=["transaction"])


@app.get('/')
def home():
    return {"message": "welcome to UserMoney"}
