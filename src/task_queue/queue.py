from utils.service import AbstractService
from utils.singleton import Singleton


class TaskQueue(AbstractService):
    def __init__(self) -> None:
        print("Queue init")

    async def run(self) -> None:
        print("Queue run")
