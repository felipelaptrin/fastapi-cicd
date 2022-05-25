from api.models.user import User
from api.schemas.user import UserInfo

def find_user_by_id(id: int) -> User:
    try:
        query = User.select().where(User.id == id)
        return query.get()
    except:
        return None


def add_user(user: UserInfo) -> User:
    added_user = User.create(**dict(user))
    return added_user


def delete_user_by_id(id: int) -> User:
    user = User.get(User.id == id)
    user.delete_instance()
    return user


def update_user_by_id(id: int, to_update: dict) -> User:
    query = User.update(**dict(to_update)).where(User.id==id)
    query.execute()