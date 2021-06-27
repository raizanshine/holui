import typing
from typing import Type

from src.connections.source_connection import SourceConnection
from src.pages import AdminPage
from src.data_source import DataSource


class AdminSite:
    name = ""
    connection: SourceConnection

    def __init__(self, name, connection: SourceConnection):
        self.name = name
        self.connection = connection
        self.pages = {}

    def __iter__(self):
        return iter(self.pages.items())

    def register(self, source_id: typing.Any, admin: Type[AdminPage]):
        data_source = self.create_data_source(source_id)
        self.pages[data_source.get_label()] = admin(source=data_source)

    def create_data_source(self, source):
        return DataSource(source, connection=self.connection)
