import datetime as dt

from marshmallow import Schema, fields


class Result():
      def __init__(self, description, stats, maps, errors):
    self.description = description
    self.stats = stats
    self.maps = maps
    self.errors = errors
    self.created_at = dt.datetime.now()

  def __repr__(self):
    return '<Result(name={self.description!r})>'.format(self=self)


class ResultSchema(Schema):
  description = fields.Str()
  stats = fields.Dict()
  maps = fields.Dict()
  errors = fields.Dict()
  created_at = fields.Date()