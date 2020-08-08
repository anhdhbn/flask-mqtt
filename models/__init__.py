import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs
import json

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()

def init_app(app, **kwargs):
    db.app = app
    db.init_app(app)
    migrate.init_app(app)

from sqlalchemy.inspection import inspect
class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
        
from .example import ExampleData