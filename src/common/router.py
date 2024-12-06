import abc
from enum import Enum
from typing import Callable

from fastapi import APIRouter


class HttpMethod(str, Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"


class BaseRouter:
    def __init__(self, name: str | None = None) -> None:
        self._router = APIRouter(prefix=(f"/{name}" if name is not None else ""))
        self.register_handlers()

    def register_route(self, path: str, handler: Callable, method: HttpMethod) -> None:
        self._router.add_api_route(path=path, endpoint=handler, methods=[method.value])

    @abc.abstractmethod
    def register_handlers(self) -> None:
        pass

    @property
    def fastapi_router(self) -> APIRouter:
        return self._router
