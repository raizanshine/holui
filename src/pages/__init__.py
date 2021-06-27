from typing import Dict

from marshmallow.fields import Field

from src.data_source import DataSource


class AdminPage:
    """
    Represents requirements for admin page in a common way.
    This specification is same for every Engine class.
    """

    def __init__(self, source: DataSource):
        self._data_source = source

    def get_fields(self) -> Dict[str, Field]:
        source_fields = self._data_source.get_fields()
        return source_fields
