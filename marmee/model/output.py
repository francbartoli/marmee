import datetime as dt

from marshmallow import Schema, fields


class Output():
	def __init__(self, item):
		self.item = item

	def __repr__(self):
    	return '<Output(item={self.item.id!r})>'.format(self=self)


class OutputSchema(Schema):
	item = fields.Method('get_item', deserialize='load_item')


	def	get_item(self, obj):
		try:
			isinstance(obj, Item)
			return obj.dict
		except ValidationError as e:
			raise
	
	def load_item(self, obj):
		return obj.json
