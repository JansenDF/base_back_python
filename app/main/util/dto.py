
from flask_restx import Namespace, fields


class LogDto:
    api = Namespace('log', description='log related operations')
    log = api.model('log', {
        'responsible_code': fields.Integer(required=True, description='foreign key user id'),
        'table': fields.String(required=True, description='table type'),
        'operation_code': fields.Integer(required=True, description='code operation'),
        'description': fields.String(description='description')
    })