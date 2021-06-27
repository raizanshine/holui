import abc

from src.connections.source_connection import SourceConnection


class DataSource:
    """
    Describes data model properties from physical layer
    """

    def __init__(self, identifier, connection: SourceConnection):
        self.id = identifier
        self.connection = connection

    def get_fields(self):
        """
        Returns field list which uses by admin page as a base declaration
        """
        return self.connection.get_fields(self.id)

    def get_label(self):
        return self.id
