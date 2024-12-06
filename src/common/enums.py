from enum import Enum


class TaskType(str, Enum):
    Mock = "mock"


class StatusType(str, Enum):
    IN_QUEUE = "in_queue"
    RUN = "run"
    COMPLETED = "completed"
