from typing import Dict

import psycopg2
from marshmallow.fields import Field

from src.connections.dialects.postgresql.field_describer import PostgresqlFieldDescriber
from src.connections.source_connection import SourceConnection


class PostgresqlSourceConnection(SourceConnection):
    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.describer = PostgresqlFieldDescriber()

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
