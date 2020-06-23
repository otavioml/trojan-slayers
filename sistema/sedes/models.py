from sistema import db
from sistema.livros.models import Disponibilidade

class Sede(db.Model):
    __tablename__ = 'sede'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    contact = db.Column(db.String)
    picture = db.Column(db.String)
    schedule = db.Column(db.String)
    livros = db.relationship('Livro', secondary=Disponibilidade, back_populates='sedes')

    def __init__(self, name, address, contact, schedule, picture):
        self.name = name
        self.address = address
        self.contact = contact
        self.schedule = schedule
        self.picture = picture

    def __repr__(self):
        return f'<Sede {self.name}>'


