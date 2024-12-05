from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server

from utils.service import AbstractService


class Producer(AbstractService):
    def __init__(self) -> None:
        self._app = FastAPI()
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def get_app(self) -> FastAPI:
        return self._app

    async def run(self) -> None:
        await ProducerServer(self).run()


class ProducerServer(Server):
    def __init__(self, producer: Producer) -> None:
        super().__init__(Config(producer.get_app(), host="0.0.0.0", port=8000))

    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)
