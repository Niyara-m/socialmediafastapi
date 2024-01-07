from database.models import User
from database import get_db

__all__ = ['registration', 'get_exact_user', 'check_password_db',
           'change_info_db', 'upload_or_change_profile_photo', 'delete_profile_photo',
           'delete_user']


# регистрация
def registration(name: str, surname: str, email: str, password: str,
                 city: str, birthday: str, profile_photo: str, **kwargs):
    db = next(get_db())
    new_user = User(name=name, surname=surname, email=email, password=password,
                    city=city, birthday=birthday, profile_photo=profile_photo)
    db.add(new_user)
    db.commit()
    return {'status':201, 'message': f'пользователь {new_user.name} создан!'}


# Получить определенного пользователя
def get_exact_user(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    return False


# проверка пароля
def check_password_db(email, password):
    db = next(get_db())
    usr_pwd = db.query(User).filter_by(email=email, password=password).first()

    if usr_pwd:
        return True
    return False


# изменить данные о себе
def change_info_db(user_id, change_info, new_data):
    db = next(get_db())
    user =db.query(User).filter_by(user_id=user_id).first()

    if user:

        # match change_info:
        #     case 'surname':
        #         user.surname = new_data
        #

        if change_info == 'surname':
            user.surname = new_data
        elif change_info == 'name':
            user.name = new_data
        elif change_info == 'city':
            user.city = new_data

        db.commit()
        return {'status': 200, 'message': 'Успешно все изменено'}
    return {'status': 404, 'message': 'пол-ля нет'}


# изменить фото или Добавить фото
def upload_or_change_profile_photo(user_id: int, new_filename: str):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = new_filename
        db.commit()
        return True
    return False


# Удалить фото
def delete_profile_photo(user_id: int):
    db = next(get_db())

    exact_photo = db.query(User).filter_by(user_id=user_id).first()
    if exact_photo:
        exact_photo.profile_photo = None
        db.commit()
        return True

    return False


# Удалить профиль пользователя
def delete_user(user_id: int):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        db.delete(exact_user)
        db.commit()

        return True
    return False

# Заблокировать пользователя

# Разблокировать пользователя


