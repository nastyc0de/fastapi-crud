from fastapi import FastAPI, HTTPException
from models import Post
from uuid import uuid4 as uuid

app = FastAPI()
all_posts = []

@app.get('/')
def home():
    return{'welcome': 'welcome to my rest API'}

@app.get('/posts')
def posts():
    return all_posts

@app.post('/posts')
def set_post(post:Post):
    post.id = str(uuid())
    all_posts.append(post.dict())
    return all_posts[-1]

@app.get('/posts/{id}')
def get_post(id: str):
    for post in all_posts:
        if post['id'] == id:
            return post
    return HTTPException(status_code=404, detail='Post no encontrado')

@app.delete('/posts/{id}')
def delete_post(id: str):
    for index, post in enumerate(all_posts):
        if post['id'] == id:
            all_posts.pop(index)
            return 'post eliminado'
    raise HTTPException(status_code=404, detail='Post not found')

@app.put('/posts/{id}')
def update_post(id:str, updatedPost: Post):
    for index, post in enumerate(all_posts):
        if post['id'] == id:
            all_posts[index]['title'] = updatedPost.title
            all_posts[index]['content'] = updatedPost.content
            all_posts[index]['author'] = updatedPost.author
            return 'post editado'
    raise HTTPException(status_code=404, detail='post no encontrado')