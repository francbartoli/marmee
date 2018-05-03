# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import fields, Schema, post_load
from marshmallow_oneofschema import OneOfSchema


class SpatialRule(object):
    def __init__(self, extent):
        self.extent = extent


class TemporalRule(object):
    def __init__(self, daterange):
        self.daterange = daterange


class SpatialRuleSchema(Schema):
    extent = fields.Dict(required=True)

    @post_load
    def make_extent(self, data):
        return SpatialRule(**data)


class Range(object):
    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date


class RangeSchema(Schema):
    from_date = fields.DateTime()
    to_date = fields.DateTime()


class TemporalRuleSchema(Schema):
    daterange = fields.Nested(RangeSchema, required=True)

    @post_load
    def make_daterange(self, data):
        return TemporalRule(**data)


class ExtentSchema(OneOfSchema):
    type_schemas = {
        'spatial': SpatialRuleSchema,
        'temporal': TemporalRuleSchema,
    }

    def get_obj_type(self, obj):
        if isinstance(obj, SpatialRule):
            return 'spatial'
        elif isinstance(obj, TemporalRule):
            return 'temporal'
        else:
            raise Exception('Unknown object type: %s' % obj.__class__.__name__)


class Rule(object):
    def __init__(self, identifier, rule):
        self.identifier = identifier
        self.rule = rule


class RuleSchema(Schema):
    identifier = fields.Str()
    rule = fields.Nested(ExtentSchema)
