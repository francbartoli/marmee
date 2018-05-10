from marshmallow import (
    Schema,
    fields
)


class MarmeeObject(object):

    def __init__(self, marmee):
        self.marmee = marmee

    @property
    def dict(self):
        return self.marmee

    @property
    def json(self):
        return MarmeeObjectSchema().dumps(
            self
        )


class MarmeeObjectSchema(Schema):

    marmee = fields.Dict()
