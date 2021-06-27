import re
from typing import Dict

import psycopg2
import psycopg2.extras
from marshmallow.fields import Field

from src.connections.dialects.postgresql.field_describer import PostgresqlFieldDescriber
from src.connections.source_connection import SourceConnection


class DatabaseSourceConnection(SourceConnection):
    connection_uri_regexp = r"(?P<schema>.*)://(?P<user>.*):(?P<password>.*)@(?P<host>.*):(?P<port>.*)/(?P<db_name>.*)"

    def __init__(self, connection_uri: str):
        super().__init__()
        match = self.parse_connection_uri(connection_uri)
        if match["schema"] == "postgresql":
            self.connection = psycopg2.connect(
                database=match["db_name"],
                user=match["user"],
                password=match["password"],
                host=match["host"],
                port=match["port"],
            )
            self.describer = PostgresqlFieldDescriber()
        else:
            raise AttributeError("Only postgresql schema available for now")

    def parse_connection_uri(self, connection_uri) -> Dict[str, str]:
        match = re.match(self.connection_uri_regexp, connection_uri)
        if match is None:
            raise AttributeError(
                "Connection query is incorrect. Please, check if it "
                "complies with the following format: "
                "schema://user:password@host:port/database_name"
            )

        return match.groupdict()

    def get_fields(self, identifier: str) -> Dict[str, Field]:
        cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            "SELECT * FROM information_schema.columns WHERE table_name = %s;",
            (identifier,),
        )
        return {
            row["column_name"]: self.describer.describe_with_information_schema(row)
            for row in cur
        }
