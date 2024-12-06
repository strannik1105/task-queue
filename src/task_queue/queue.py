from task_queue.task_pool import TaskPool
from common.service import AbstractService


class TaskQueue(AbstractService):
    def __init__(self) -> None:
        self._task_pool = TaskPool()

    async def run(self) -> None:
        await self._task_pool.run()
