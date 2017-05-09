from elasticsearch_dsl.field import (
    Keyword,
    Text,
)
from .base import DEDField


class KeywordField(DEDField, Keyword):
    pass


class TextField(DEDField, Text):
    pass
