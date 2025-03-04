from app.repositories.post_respository import PostRepository


class PostService:
    @staticmethod
    def create(title, content, user_id):
        return PostRepository.create_post(title, content, user_id)

    @staticmethod
    def get_all():
        return PostRepository.get_all_posts()

    @staticmethod
    def get_by_id(id):
        return PostRepository.get_post_by_id(id)

    @staticmethod
    def update(id, title, content):
        return PostRepository.update_post(id, title, content)

    @staticmethod
    def delete(id):
        return PostRepository.delete_post(id)
