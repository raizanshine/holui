from marshmallow import fields

from src.connections.dialects.field_describer import FieldDescriber


field_mapper = {
    "integer": fields.Integer,
    "smallint": fields.Integer,
    "character varying": fields.String,
}


class PostgresqlFieldDescriber(FieldDescriber):
    def describe_with_information_schema(self, row: dict):
        field_class = field_mapper[row["data_type"]]
        return field_class(**self.get_field_kwargs(row))

    def get_field_kwargs(self, row: dict):
        kwargs = {}
        if row["is_nullable"]:
            kwargs["required"] = True
        return {}
