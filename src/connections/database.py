import re

from src.connections.dialects.postgresql.connection import PostgresqlSourceConnection

connection_uri_regexp = r"(?P<schema>.*)://(?P<user>.*):(?P<password>.*)@(?P<host>.*):(?P<port>.*)/(?P<db_name>.*)"


def get_database_connection(connection_uri: str):
    match = re.match(connection_uri_regexp, connection_uri)
    if match is None:
        raise AttributeError(
            "Connection query is incorrect. Please, check if it "
            "complies with the following format: "
            "schema://user:password@host:port/database_name"
        )

    match = match.groupdict()
    if match["schema"] == "postgresql":
        connection = PostgresqlSourceConnection(
            database=match["db_name"],
            user=match["user"],
            password=match["password"],
            host=match["host"],
            port=match["port"],
        )
    else:
        raise AttributeError("Only postgresql schema available for now")

    return connection
