from app.repositories.category_respository import CategoryRespository


class CategoryService:
    @staticmethod
    def create(name):
        return CategoryRespository.create_category(name)

    @staticmethod
    def get_all():
        return CategoryRespository.get_all_categories()

    @staticmethod
    def get_by_id(id):
        return CategoryRespository.get_category_by_id(id)

    @staticmethod
    def update(id, name):
        return CategoryRespository.update_category(id, name)

    @staticmethod
    def delete(id):
        return CategoryRespository.delete_category(id)
