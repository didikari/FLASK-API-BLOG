from app.extensions import db
from app.models.base import BaseModel

class Post(BaseModel):
    __tablename__ = "posts"

    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", backref="posts")
