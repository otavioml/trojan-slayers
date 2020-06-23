from sistema import db

Disponibilidade = db.Table('disponibilidade',
                           db.Column('livro_id', db.Integer, db.ForeignKey('livro.id')),
                           db.Column('sede_id', db.Integer, db.ForeignKey('sede.id')))

class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    gender = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.String)
    pub_date = db.Column(db.String)
    available = db.Column(db.Boolean)
    cover = db.Column(db.String)
    sedes = db.relationship('Sede', secondary=Disponibilidade, back_populates='livros')

    def __init__(self, title, gender, author, price, pub_date, available, cover):
        self.title = title
        self.gender = gender
        self.author = author
        self.price = price
        self.pub_date = pub_date
        self.available = available
        self.cover = cover

    def __repr__(self):
        return f'<Livro {self.title}>'

