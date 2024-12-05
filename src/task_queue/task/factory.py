from enum import Enum

from task_queue.task.abstract_task import AbstractTask
from task_queue.task.mock_task import MockTask


class TaskType(str, Enum):
    Mock = "mock"


TASK_MAPPER = {TaskType.Mock: MockTask}


class TaskFactory:
    @staticmethod
    def get_task(type_: TaskType) -> AbstractTask:
        return TASK_MAPPER[type_]()
