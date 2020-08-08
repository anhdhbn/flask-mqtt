from sqlalchemy import func
from models import db
from sqlalchemy import Float
import uuid
from . import Serializer

class ExampleData(db.Model, Serializer):
    __tablename__ = 'example_table'
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    id = db.Column(db.String(64), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    temperature = db.Column(Float(), default=False, nullable=False)

    def __repr__(self):
        return f'<Temp: {self.temperature}°C>'

    def serialize(self):
        return Serializer.serialize(self)