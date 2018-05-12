# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import Schema, fields
from .base import MarmeeObject
from .rule import RuleSchema
import json


class Filter(MarmeeObject):
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def __repr__(self):
        return '<Filter(name={self.name!r})>'.format(self=self)

    @property
    def dict(self):
        return dict(
            name=self.name,
            rules=[rule.dict for rule in self.rules]
        )

    @property
    def json(self):
        # return FilterSchema().dumps(
        #     self
        # )
        return json.dumps(self.dict)


class FilterSchema(Schema):
    name = fields.Str()
    rules = fields.Nested(RuleSchema, many=True)
