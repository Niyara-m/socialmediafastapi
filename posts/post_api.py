from fastapi import APIRouter, HTTPException
from database.postservice import add_new_post, unlike_post, change_post_text, \
    like_post, delete_post, get_exact_post, get_exact_user_posts


# создать компонент
post_router = APIRouter(prefix='/post')


# Запрос на создание поста
@post_router.post('/new-post')
async def new_post_api(user_id: int, post_text: str):
    result = add_new_post(user_id=user_id, post_text=post_text)

    if result:
        return {'status': 200, 'message': 'Пост успешно опубликован'}

    raise HTTPException(status_code=404, detail='Ошибка в данных')


# Поставить лайк к посту
@post_router.put('/like-post')
async def like_post_api(post_id: int):
    result = like_post(post_id=post_id)

    if result:
        return {'status': 200, 'message': 'Лайк поставлен'}

    raise HTTPException(status_code=404, detail='Пост не найден')


# Убрать лайк из поста
@post_router.put('/unlike-post')
async def unlike_post_api(post_id: int):
    result = unlike_post(post_id=post_id)

    if result:
        return {'status': 200, 'message': 'Лайк убран'}

    raise HTTPException(status_code=404, detail='Пост не найден')


# Изменить текст поста
@post_router.put('/change-text')
async def change_post_text_api(post_id: int, new_text: str):
    result = change_post_text(post_id=post_id, new_text=new_text)

    if result:
        return {'status': 200, 'message': 'Пост успешно изменен'}

    raise HTTPException(status_code=404, detail='Пост не найден')


# Удалить определенный пост
@post_router.delete('/delete-post')
async def delete_post_api(post_id: int):
    result = delete_post(post_id=post_id)

    if result:
        return {'status': 200, 'message': 'Пост удален'}

    raise HTTPException(status_code=404, detail='Пост не найден')


# Вывести информацию про определенный пост
@post_router.get('/exact-posts')
async def get_exact_post_api(post_id: int):
    result = get_exact_post(post_id=post_id)

    if result:
        return {'status': 200, 'message': result}

    raise HTTPException(status_code=404, detail='Пост не найден')


# Вывести весь список постов
@post_router.get('/exact-user-posts')
async def get_exact_user_posts_api(user_id: int):
    result = get_exact_user_posts(user_id=user_id)

    if result:
        return {'status': 200, 'message': result}

    raise HTTPException(status_code=404, detail='Пользователь не найден')