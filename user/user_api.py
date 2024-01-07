from fastapi import APIRouter, UploadFile, HTTPException
from starlette import status
from user import User
from database.userservice import *


# создать компонент
user_router = APIRouter(prefix='/user', tags=['Работа с пользователем'])


@user_router.post('/regiistration')
async def register_user(data: User):
    data_dump = data.model_dump()
    new_user = registration(**data_dump)
    return new_user


@user_router.get('/get-exact-user')
async def get_user_by_id(user_id: int):
    user = get_exact_user(user_id=user_id)
    if user:
        return {'status': 200, 'message': user}
    return {'status': 404, 'message': 'User not found'}


@user_router.get('/get=password')
async def check_password(email:str, password:str):
    user = check_password_db(email=email, password=password)
    return {'status': 200, 'message': user}


@user_router.put('/change-profile')
async def change_profile(user_id: int, change_info:str, new_data:str):
    try_change = change_info_db(user_id, change_info,new_data)
    return try_change


@user_router.put('/change-profile-photo')
async def change_profile_photo(user_id: int, file: UploadFile):
    # сохранение фото в локальную попку
    file_open = await file.read()
    new_file = open(file.filename, 'wb')
    new_file.write(file_open)
    new_file.close()

    # вызов функции изменения фото
    result = upload_or_change_profile_photo(user_id, file.filename)

    if result:
        return {'status':200, 'message': 'Фото успешно добавлено'}

    # если не находит пол-ля то
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@user_router.delete('/delete-profile-photo')
async def delete_profile_photo(user_id: int):
    result = delete_profile_photo(user_id)

    if result:
        return {'status': 200, 'message': 'Успешно удалено'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')


@user_router.delete('/delete-user-profile')
async def delete_exact_usero(user_id: int):
    result = delete_user(user_id)

    if result:
        return {'status': 200, 'message': 'Успешно удалено'}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Пользователь не найден')