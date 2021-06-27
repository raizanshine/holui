import abc

from marshmallow.fields import Field


class FieldDescriber(abc.ABC):
    @abc.abstractmethod
    def describe_with_information_schema(self, row: dict):
        return Field()
