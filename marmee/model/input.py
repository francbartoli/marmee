import datetime as dt

from marshmallow import Schema, fields


class Input():
	def __init__(self, process, arguments):
		self.process = process
		self.arguments = arguments
		self.created_at = dt.datetime.now()

	def __repr__(self):
		return '<Input(process={self.process!r})>'.format(self=self)


class ArgumentSchema(Schema):
	positional = fields.Bool()
	identifier = fields.Str()
	values = fields.List()

class InputSchema(Schema):
	process = fields.Str()
	arguments = fields.Nested(ArgumentSchema, many=True)
	created_at = fields.Date()
