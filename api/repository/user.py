from api.models.user import User


def find_user_by_id(id: int) -> User:
    try:
        query = User.select().where(User.id == id)
        return query.get()
    except:
        return None