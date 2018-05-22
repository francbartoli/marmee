# Copyright (c) 2018 Francesco Bartoli
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# -*- coding: utf-8 -*-
from .abstract_marmee import AbstractMarmee
from marshmallow import fields, Schema, ValidationError
from .model.base import MarmeeObject
from .model.input import InputSchema
from .model.output import OutputSchema
from .model.filter import FilterSchema
import json


class Marmee(AbstractMarmee, MarmeeObject):

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
                self._inputs.append(arg)
            except ValidationError as e:
                raise

    @property
    def filters(self):
        return self._filters

    @filters.setter
    def set_filters(self, *args):
        for arg in args:
            try:
                self._filters.append(arg)
            except ValidationError as e:
                raise

    @property
    def outputs(self):
        return self._outputs

    @outputs.getter
    def get_outputs(self):
        return self.outputs

    @outputs.setter
    def set_outputs(self, *args):
        for arg in args:
            try:
                self._outputs.append(arg)
            except ValidationError as e:
                raise

    def get_name(self):
        return self.name

    def is_marmee(self):
        pass

    @property
    def dict(self):
        return dict(
            name=self.name,
            inputs=[input.dict for input in self.inputs],
            filters=[filter.dict for filter in self.filters],
            outputs=[output.dict for output in self.outputs],
        )

    @property
    def json(self):
        # return MarmeeSchema().dumps(
        #     self
        # )
        return json.dumps(self.dict)


class MarmeeSchema(Schema):
    name = fields.Str()
    inputs = fields.Nested(InputSchema, many=True)
    filters = fields.Nested(FilterSchema, many=True)
    outputs = fields.Nested(OutputSchema, many=True)
