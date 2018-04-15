import datetime as dt

from marshmallow import Schema, fields


class Output():
  def __init__(self, description, stats, maps, errors):
    self.description = description
    self.stats = stats
    self.maps = maps
    self.errors = errors
    self.created_at = dt.datetime.now()

  def __repr__(self):
    return '<Output(name={self.description!r})>'.format(self=self)

class MapSchema(Schema):
  product = fields.String()
  token = fields.String()
  mapid = fields.String()
  image = fields.Dict()
  

class OutputSchema(Schema):
  description = fields.Str()
  stats = fields.Dict()
  maps = fields.Nested(MapSchema, many=True)
  errors = fields.Dict()
  created_at = fields.Date()