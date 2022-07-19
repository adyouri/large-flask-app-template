from app.extensions import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    answer = db.Column(db.Text)

    def __repr__(self):
        return f'<Question {self.content}>'
