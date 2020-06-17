from sistema import db

class Novidade(db.Model):
    __tablename__ = 'novidade'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author = db.Column(db.String)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f'<Novidade {self.title}>'
