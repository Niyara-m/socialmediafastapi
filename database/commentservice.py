from database.models import PostComment
from database import get_db


# Написать коммент
def add_new_comment(post_id, user_id, comment_text):
    db = next(get_db())
    new_comment = PostComment(post_id=post_id, user_id=user_id, comment_text=comment_text)
    db.add(new_comment)
    db.commit()

    return True


# Изменить коммент
def change_comment_text(comment_id, new_comment):
    db = next(get_db())
    comment = db.query(PostComment).filter_by(comment_id=comment_id).first()
    if comment:
        comment.comment_text = new_comment
        db.commit()
        return True
    return False


# Удалить коммент
def delete_post_comment(comment_id):
    db = next(get_db())
    comment = db.query(PostComment).filter_by(comment_id=comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()


# Получить все комментарии к определенному посту
def get_post_comments(post_id):
    db = next(get_db())
    post_comments = db.query(PostComment).filter_by(post_id=post_id).all()
    return post_comments