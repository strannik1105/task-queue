from redis_om import Migrator  # type: ignore

from common.enums import TaskType
from common.singleton import Singleton
from task_storage.abstract_task_storage import AbstractTaskStorage
from task_storage.redis.models import Task


class RedisTaskStorage(AbstractTaskStorage, Singleton[AbstractTaskStorage]):
    migrated = False

    def init(self) -> None:
        if not self.migrated:
            Migrator.run()
            self.migrated = True

    async def make_task(
        self, task_type: TaskType, task_params: dict | None = None
    ) -> str:
        task = Task(type=task_type, params=task_params)
        await task.save()
        return task.pk
