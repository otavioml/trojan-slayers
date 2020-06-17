from sistema import db

class Sede(db.Model):
    __tablename__ = 'sede'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    contact = db.Column(db.String)
    picture = db.Column(db.String)

    def __init__(self, name, address, contact, picture):
        self.name = name
        self.address = address
        self.contact = contact
        self.picture = picture

    def __repr__(self):
        return f'<Sede {self.name}>'


