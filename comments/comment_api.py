from fastapi import APIRouter, HTTPException
from database.commentservice import add_new_comment, get_post_comments, \
    delete_post_comment, change_comment_text


# создать компонент
comment_router = APIRouter(prefix='/comment')


# Добавить коммент
@comment_router.post('/add-comment')
async def add_comment_api(post_id: int, user_id: int, comment_text: str):
    result = add_new_comment(post_id=post_id, user_id=user_id, comment_text=comment_text)

    if result:
        return {'status': 200, 'message': 'Коммент опубликован'}

    raise HTTPException(status_code=404, detail='Ошибка в данных')


# Получить все комменты поста
@comment_router.get('/get-comment')
async def get_comment_api(post_id):
    result = get_post_comments(post_id=post_id)

    if result:
        return {'status': 200, 'message': result}

    raise HTTPException(status_code=404, detail='коммент не найден')


# Удалить опред коммент
@comment_router.delete('/delete-comment')
async def delete_comment_api(comment_id: int):
    result = delete_post_comment(comment_id=comment_id)

    if result:
        return {'status': 200, 'message': 'Коммент удален'}

    raise HTTPException(status_code=404, detail='Коммент не найден')


# Изменить опред коммент
@comment_router.put('/change-comment')
async def change_comment_api(comment_id: int, new_comment: str):
    result = change_comment_text(comment_id=comment_id, new_comment=new_comment)

    if result:
        return {'status': 200, 'message': 'Коммент успешно изменен'}

    raise HTTPException(status_code=404, detail='Коммент не найден')