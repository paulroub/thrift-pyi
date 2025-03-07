from dataclasses import dataclass
from typing import *

class NotFound(Exception):
    message: Optional[str] = "Not Found"

class EmptyException(Exception):
    pass

@dataclass
class LimitOffset:
    limit: Optional[int] = None
    offset: Optional[int] = None

class Service:
    async def ping(self,) -> str: ...
