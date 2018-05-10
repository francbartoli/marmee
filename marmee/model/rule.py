# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import fields, Schema, post_load
from .base import MarmeeObject
from marshmallow_oneofschema import OneOfSchema


class SpatialRule(MarmeeObject):
    def __init__(self, extent):
        self.extent = extent

    @property
    def dict(self):
        return dict(
            extent=self.extent
        )

    @property
    def json(self):
        return SpatialRuleSchema().dumps(
            self
        )


class TemporalRule(MarmeeObject):
    def __init__(self, daterange):
        self.daterange = daterange

    @property
    def dict(self):
        return dict(
            daterange=self.daterange
        )

    @property
    def json(self):
        return TemporalRuleSchema().dumps(
            self
        )


class SpatialRuleSchema(Schema):
    extent = fields.Dict(required=True)

    @post_load
    def make_extent(self, data):
        return SpatialRule(**data)


class Range(MarmeeObject):
    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date

    @property
    def dict(self):
        return dict(
            from_date=self.from_date,
            to_date=self.to_date
        )

    @property
    def json(self):
        return RangeSchema().dumps(
            self
        )


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


class Rule(MarmeeObject):
    def __init__(self, identifier, rule):
        self.identifier = identifier
        self.rule = rule

    @property
    def dict(self):
        return dict(
            identifier=self.identifier,
            rule=self.rule
        )

    @property
    def json(self):
        return RuleSchema().dumps(
            self
        )


class RuleSchema(Schema):
    identifier = fields.Str()
    rule = fields.Nested(ExtentSchema)
