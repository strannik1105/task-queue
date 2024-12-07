from typing import Annotated

from fastapi import Depends

from task_storage.abstract_task_storage import AbstractTaskStorage
from task_storage.redis_task_storage import RedisTaskStorage as _RedisTaskStorage


RedisTaskStorage = Annotated[AbstractTaskStorage, Depends(_RedisTaskStorage)]
