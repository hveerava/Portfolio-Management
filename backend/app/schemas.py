from marshmallow import Schema, fields

class InvestmentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    date = fields.Date(required=True)
