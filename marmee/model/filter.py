import datetime as dt

from marshmallow import Schema, fields


class Filter():
      def __init__(self, name, rules):
    self.name = name
    self.rules = rules

  def __repr__(self):
    return '<Filter(name={self.name!r})>'.format(self=self)


class FilterSchema(Schema):
  name = fields.Str()
  rules = fields.List()
  created_at = fields.Date()