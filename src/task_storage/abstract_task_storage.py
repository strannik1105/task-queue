import abc
from typing import Any

from common.enums import StatusType, TaskType


class AbstractTaskStorage(abc.ABC):
    @abc.abstractmethod
    async def init(self) -> None:
        pass

    @abc.abstractmethod
    async def make_task(
        self, task_type: TaskType, task_params: dict | None = None
    ) -> str:
        pass

    @abc.abstractmethod
    async def get_task(self) -> Any:
        pass

    @abc.abstractmethod
    async def change_task_status(self, key: str, status: StatusType) -> None:
        pass
