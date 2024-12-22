from marshmallow import Schema, fields


class QuestionSchema(Schema):
    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(required=True)
    created_at = fields.DateTime()
