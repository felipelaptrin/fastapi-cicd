from api.models.user import User


def find_user_by_id(id: int) -> User:
    query = User.select().where(User.id == id)
    return query.get()
