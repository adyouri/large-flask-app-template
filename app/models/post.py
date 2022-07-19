from app.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post "{self.title}">'
