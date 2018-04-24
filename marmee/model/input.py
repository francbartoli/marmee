from marshmallow import Schema, fields
from marmee.model.filter import FilterSchema
from pystac.models.item import Item


class Input():
	def __init__(self, item, filters):
		self.item = item
		self.filters = filters

	def __repr__(self):
		return '<Input(item={self.item.id!r})>'.format(self=self)


class InputSchema(Schema):
	item = fields.Method('get_item', deserialize='load_item')
	filters = fields.Nested(FilterSchema, many=True)


	def	get_item(self, obj):
		try:
			isinstance(obj, Item)
			return obj.dict
		except ValidationError as e:
			raise
	
	def load_item(self, obj):
		return obj.json
