from sistema import db

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

class Disponibilidade(db.Model):
    __tablename__ = 'disponibilidade'

    id = db.Column(db.Integer, primary_key=True)
    livroid = db.Column(db.Integer)
    sedeid = db.Column(db.Integer)

    def __init__(self, livroid, sedeid):
        self.livroid = livroid
        self.sedeid = sedeid