from . import db
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, Text, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY


class Unparsed(db.Model):
    __tablename__ = 'unparsed_hl7'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    date_created = Column(DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return '<Unparsed Data %r>' % self.id
