import datetime as dt

from marshmallow import Schema, fields


class Filter():
	def __init__(self, name, rules):
		self.name = name
		self.rules = rules

	def __repr__(self):
		return '<Filter(name={self.name!r})>'.format(self=self)


class RuleSchema(Schema):
	identifier = fields.Str()
	description = fields.Str()
	rule = fields.Dict()

class FilterSchema(Schema):
	name = fields.Str()
	rules = fields.Nested(RuleSchema, many=True)
	created_at = fields.Date()
