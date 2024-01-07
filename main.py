from fastapi import FastAPI
from photos.photo_api import photo_router
import uvicorn
from user.user_api import user_router
from posts.post_api import post_router
from database import Base, engine
from comments.comment_api import comment_router

Base.metadata.create_all(bind=engine)


app = FastAPI()


# Региcтрация компонентов
app.include_router(user_router)
app.include_router(post_router, tags=['Работа с постами'])
app.include_router(photo_router, tags=['Работа с фото'])
app.include_router(comment_router, tags=['Работа с комментариями'])


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)