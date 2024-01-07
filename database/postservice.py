from sqlalchemy import delete
from database.models import Post, PostPhoto
from database import get_db


# Загрузить текст поста
def add_new_post(user_id: int, post_text: str):
    db = next(get_db())
    new_post = Post(user_id=user_id, post_text=post_text)
    db.add(new_post)
    db.commit()
    return True


# Загрузить фото поста
def add_post_photo(post_id: int, photo_path: str):
    db = next(get_db())
    post = db.query(Post).filter_by(id=post_id).first()
    if post:
        new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)
        db.add(new_photo)
        db.commit()
        return True
    return False


# Изменить текст поста
def change_post_text(post_id: int, new_text: str):
    db = next(get_db())
    post = db.query(Post).filter_by(id=post_id).first()
    if post:
        post.post_text = new_text
        db.commit()
        return True
    return False


# Удалить весь пост (фото и текст)
def delete_post(post_id:int):
    db = next(get_db())
    exact_post = db.query(Post).filter_by(post_id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        exact_post_photos = db.query(PostPhoto).filter_by(post_id=post_id).all()

        if exact_post_photos:
            delete(exact_post_photos)

        db.commit()

        return True
    return False


# Поставить лайк
def like_post(post_id: int):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()

        return True

    return False


# Убрать лайк
def unlike_post(post_id: int):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(post_id=post_id).first()

    if exact_post and exact_post.likes > 0:
        exact_post.likes -= 1
        db.commit()

        return True

    return False


# Получить все посты определенного пользователя
def get_exact_user_posts(user_id):
    db = next(get_db())

    exact_user = db.query(Post).filter_by(user_id=user_id).all()

    return exact_user


# Получить информацию об определленом посте
def get_exact_post(post_id):
    db = next(get_db())

    exact_post = db.query(Post).filter_by(post_id=post_id).first()

    return exact_post


# Получить все фото определенного поста
def get_post_photos(post_id: int):
    db = next(get_db())

    exact_post_photos = db.query(PostPhoto).filter_by(post_id=post_id).all()

    return exact_post_photos
