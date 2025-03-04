from app.models.post import Post
from app.extensions import db


class PostRepository:
    @staticmethod
    def create_post(title, content, user_id):
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def get_all_posts():
        return Post.query.all()

    @staticmethod
    def get_post_by_id(id):
        return Post.query.get(id)

    @staticmethod
    def update_post(id, title, content):
        post = Post.query.get(id)
        post.title = title
        post.content = content
        db.session.commit()
        return post

    @staticmethod
    def delete_post(id):
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return post
