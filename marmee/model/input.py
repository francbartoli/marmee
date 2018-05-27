# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import Schema, fields, ValidationError
from .base import MarmeeObject
from .filter import FilterSchema
from pystac.models.item import Item
from pystac.models.collection import Collection
import json


class Input(MarmeeObject):
    def __init__(self, stacobject, reducers):
        self.stacobject = stacobject
        self.reducers = reducers

    def __repr__(self):
        return '<Input(stacobject={self.stacobject.id!r})>'.format(self=self)

    @property
    def dict(self):
        return dict(
            stacobject=self.stacobject.dict,
            reducers=[reducer.dict for reducer in self.reducers]
        )

    @property
    def json(self):
        # return InputSchema().dumps(
        #     self
        # )
        return json.dumps(self.dict)


class InputSchema(Schema):
    stacobject = fields.Method(
        'get_stacobject',
        deserialize='load_stacobject'
    )
    reducers = fields.Nested(FilterSchema, many=True)

    def get_stacobject(self, obj):
        try:
            isinstance(obj, Item) or isinstance(obj, Collection)
            return obj.dict
        except ValidationError as e:
            raise

    def load_stacobject(self, obj):
        return obj.json
