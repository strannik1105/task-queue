from common.service import AbstractService
from task_queue.task_pool import TaskPool
from task_storage.redis_task_storage import RedisTaskStorage


class TaskQueue(AbstractService):
    def __init__(self) -> None:
        self._task_pool = TaskPool(RedisTaskStorage())

    async def run(self) -> None:
        await self._task_pool.run()
