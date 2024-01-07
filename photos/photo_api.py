from fastapi import APIRouter, UploadFile, HTTPException

from database.postservice import add_post_photo, get_post_photos


# создать компонент
photo_router = APIRouter(prefix='/photo')


# Загрузить фото (# сохранить фото в локальный компьютер)
@photo_router.post('/add-post-photo')
async def add_photo(file: UploadFile, post_id: int):
    result = add_post_photo(post_id=post_id, photo_path=file.filename)

    # Открываем фото
    file_open = await file.read()
    # Открыть новый документ
    new_file = open(file.filename, 'wb')
    # записать содержимое файла который пришел в новый файл
    new_file.write(file_open)
    # Закрыть файл
    new_file.close()

    if result:
        return {'status': 200, 'message': 'фото успешно загружено'}

    return HTTPException(status_code=404, detail='Пост не найден')


# Получить все фото определенного поста
@photo_router.get('/get-post-photos')
async def get_post_photos_api(post_id: int):
    result = get_post_photos(post_id=post_id)

    if result:
        return {'status': 200, 'message': result}

    return HTTPException(status_code=404, detail='Фотки не найдены')
