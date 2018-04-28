# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# -*- coding: utf-8 -*-
from marmee.abstract_marmee import AbstractMarmee
from marshmallow import fields, Schema
from marmee.model.input import InputSchema, Input
from marmee.model.output import OutputSchema
from marmee.model.filter import FilterSchema, Filter


class Marmee(AbstractMarmee):

    def __init__(self, name, inputs, filters, outputs):

        self.name = name
        self.inputs = inputs
        self.filters = filters
        self.outputs = outputs

    def get_name(self):
        return self.name

    def is_marmee(self):
        pass

    def set_inputs(self, *args):
        for arg in args:
            try:
                isinstance(arg, Input)
            except ValidationError as e:
                raise
        self.inputs += args

    def get_outputs(self):
        return self.outputs

    def set_filters(self, *args):
        for arg in args:
            try:
                isinstance(arg, Filter)
            except ValidationError as e:
                raise
        self.filters += args


class MarmeeSchema(Schema):
    name = fields.Str()
    inputs = fields.Nested(InputSchema, many=True)
    filters = fields.Nested(FilterSchema, many=True)
    outputs = fields.Nested(OutputSchema, many=True)
