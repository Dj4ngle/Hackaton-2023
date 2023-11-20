from marshmallow import Schema, fields


class MapSchema(Schema):
    id = fields.Int(required=False)
    x = fields.Int(required=True)
    y = fields.Int(required=True)
    type = fields.Str(required=False)
    resource = fields.Str(required=False)

class MapListSchema(Schema):
    maps = fields.Nested(MapSchema, many=True)
