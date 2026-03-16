from fastapi import APIRouter
from functools import wraps

router = APIRouter()


def agent_endpoint(path: str):

    if not path.startswith("/"):
        path = f"/{path}"

    def decorator(func):

        @router.post(path)
        @wraps(func)
        async def endpoint(prompt: str):
            return func(prompt)

        return endpoint

    return decorator