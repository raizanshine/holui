import abc
from typing import List, Any, Dict

from marshmallow.fields import Field


class SourceConnection(abc.ABC):
    @abc.abstractmethod
    def get_fields(self, identifier: Any) -> Dict[str, Field]:
        return {}
