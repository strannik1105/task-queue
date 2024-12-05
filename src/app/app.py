import abc
import asyncio

import uvicorn

from app.config import AppConfig
from producer import Producer
from task_queue import TaskQueue
from utils import Singleton
from utils.service import AbstractService


class AbstractApp(abc.ABC):
    @abc.abstractmethod
    def run(self) -> None:
        pass


class App(Singleton[AbstractApp]):
    def __init__(self) -> None:
        config = AppConfig()

        self._host = config.HOST
        self._port = config.PORT

        self._services: list[AbstractService] = [
            Producer(),
            TaskQueue(),
        ]

    async def _run(self) -> None:
        await asyncio.gather(*[service.run() for service in self._services])

    def run(self) -> None:
        asyncio.run(self._run())
