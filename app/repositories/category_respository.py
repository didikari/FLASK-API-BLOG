from app.models.category import Category
from app.extensions import db


class CategoryRespository:
    @staticmethod
    def create_category(name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all_categories():
        return Category.query.all()

    @staticmethod
    def get_category_by_id(id):
        return Category.query.get(id)

    @staticmethod
    def update_category(id, name):
        category = Category.query.get(id)
        category.name = name
        db.session.commit()
        return category

    @staticmethod
    def delete_category(id):
        category = Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return category
