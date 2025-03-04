from app.models.category import Category
from app.extensions import db


class CategoryRespository:
    @staticmethod
    def create_category(name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
