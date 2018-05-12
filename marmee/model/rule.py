# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from marshmallow import fields, Schema, post_load
from .base import MarmeeObject
from marshmallow_oneofschema import OneOfSchema
import json


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
            from_date=self.from_date.strftime("%Y-%m-%d"),
            to_date=self.to_date.strftime("%Y-%m-%d")
        )

    @property
    def json(self):
        return RangeSchema().dumps(
            self
        )


class RangeSchema(Schema):
    from_date = fields.DateTime()
    to_date = fields.DateTime()


class TemporalRuleSchema(RangeSchema):
    daterange = fields.Dict(required=True)

    @post_load
    def make_daterange(self, data):
        return TemporalRule(**data)


# class Extent(MarmeeObject):
#     def __init__(self, t_rule, s_rule):
#         # self = TemporalRule(t_rule.dict), SpatialRule(s_rule.dict)
#         self = ExtentSchema(many=True).dump(
#             [t_rule, s_rule]
#         )

#     @property
#     def dict(self):
#         return json.loads(self)

#     @property
#     def json(self):
#         # return ExtentSchema().dump(
#         #     self, many=True
#         # )
#         return json.dumps(self.dict)


class ExtentSchema(OneOfSchema):
    type_field = 'type'
    type_field_remove = False
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
            # rule=[r.dict for r in self.rule]
            rule=self.rule
        )

    @property
    def json(self):
        # return RuleSchema().dumps(
        #     self
        # )
        return json.dumps(self.dict)


class RuleSchema(Schema):
    identifier = fields.Str()
    rule = fields.Nested(ExtentSchema)
