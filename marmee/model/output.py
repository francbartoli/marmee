# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import Schema, fields, ValidationError
from pystac.models.item import Item


class Output():
    def __init__(self, item):
        self.item = item

    def __repr__(self):
        return '<Output(item={self.item.id!r})>'.format(self=self)


class OutputSchema(Schema):
    item = fields.Method('get_item', deserialize='load_item')

    def get_item(self, obj):
        try:
            isinstance(obj, Item)
            return obj.dict
        except ValidationError as e:
            raise

    def load_item(self, obj):
        return obj.json
