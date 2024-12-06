from common.enums import TaskType
from common.schemas import AbstractSchema


class MockTaskCreateSchema(AbstractSchema):
    task_type: TaskType
    task_params: dict


class MockTaskSchema(AbstractSchema):
    task_id: str
