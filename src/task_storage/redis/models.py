from typing import Optional
from aredis_om import JsonModel, Field  # type: ignore

from common.enums import StatusType, TaskType


class Task(JsonModel):
    type: TaskType
    params: Optional[dict]
    status: StatusType = Field(StatusType.IN_QUEUE, index=True)
