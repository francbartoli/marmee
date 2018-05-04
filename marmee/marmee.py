# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# -*- coding: utf-8 -*-
from abstract_marmee import AbstractMarmee
from marshmallow import fields, Schema, ValidationError
from model.input import InputSchema, Input
from model.output import OutputSchema
from model.filter import FilterSchema, Filter


class Marmee(AbstractMarmee):

    def __init__(self, name, inputs, filters, outputs):

        self._name = name
        self._inputs = inputs
        self._filters = filters
        self._outputs = []

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, val):
        try:
            self.name = val
        except ValidationError as ve:
            raise

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def set_inputs(self, *args):
        for arg in args:
            try:
                self._inputs += arg
            except ValidationError as e:
                raise

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def set_filters(self, *args):
        for arg in args:
            try:
                self._filters += arg
            except ValidationError as e:
                raise

    @property
    def outputs(self):
        return self._outputs

    def get_name(self):
        return self.name

    def is_marmee(self):
        pass

    def get_outputs(self):
        return self.outputs


class MarmeeSchema(Schema):
    name = fields.Str()
    inputs = fields.Nested(InputSchema, many=True)
    filters = fields.Nested(FilterSchema, many=True)
    outputs = fields.Nested(OutputSchema, many=True)
