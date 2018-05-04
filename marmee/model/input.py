# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import Schema, fields, ValidationError
from .filter import FilterSchema
from pystac.models.item import Item


class Input():
    def __init__(self, item, reducers):
        self.item = item
        self.reducers = reducers

    def __repr__(self):
        return '<Input(item={self.item.id!r})>'.format(self=self)


class InputSchema(Schema):
    item = fields.Method('get_item', deserialize='load_item')
    reducers = fields.Nested(FilterSchema, many=True)

    def get_item(self, obj):
        try:
            isinstance(obj, Item)
            return obj.dict
        except ValidationError as e:
            raise

    def load_item(self, obj):
        return obj.json
