"""Data models."""
from . import db


class Produto(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'flasksqlalchemy-tutorial-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    nome = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return '<produto {}>'.format(self.nome)
