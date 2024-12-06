import abc

from pydantic import BaseModel


class AbstractSchema(BaseModel, abc.ABC):
    pass


class Msg(AbstractSchema):
    msg: str
