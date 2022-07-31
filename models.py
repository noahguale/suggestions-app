from settings import db

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    suggestions = db.relationship('Suggestion', backref='category', cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Category: {self.title}"

class Suggestion(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    author = db.Column(db.String(80))
    comments = db.relationship('Comment', backref='suggestion', cascade="all, delete-orphan")
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self) -> str:
        return f"Post by {self.author}"

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(80),nullable=False)
    suggestion_id = db.Column(db.Integer, db.ForeignKey('suggestion.id'))

    def __repr__(self) -> str:
        return f"Comment: {self.body}"
