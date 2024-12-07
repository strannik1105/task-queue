from datetime import datetime, timezone
from typing import Optional

from aredis_om import JsonModel, Field  # type: ignore

from common.enums import StatusType, TaskType


class Task(JsonModel):
    type: TaskType
    params: Optional[dict]
    status: str = Field(StatusType.IN_QUEUE.value, index=True)
    created_at: datetime = Field(datetime.now(timezone.utc), index=True)
