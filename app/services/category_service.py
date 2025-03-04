from app.repositories.category_respository import CategoryRespository


class CategoryService:
    @staticmethod
    def create(name):
        return CategoryRespository.create_category(name)
