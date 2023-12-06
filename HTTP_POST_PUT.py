#Post - апдейт
#put - создает
#get - читает
#CRUD (Create read update delete)

"""
видео урок:
https://www.youtube.com/watch?v=tTnquxuOUxc
"""

import requests

website = "https://jsonplaceholder.typicode.com/posts"


#создаем ресурс на сайте
response = requests.post(website, data={
    "userID": 12,
    "title": "My new post",
    "body": "body for my post TestPostTestPost",
})
print(response.status_code)
print(response.text)

#Можно вместо data смотреть на json как ниже. Объект, который мы передаем автоматически переделывается в json
#data - это данные
#не все объекты можно перевести в json, тогда можно перейти в data (но обратно приходит в виде json)
#создаем ресурс на сайте
response = requests.post(website, json={
    "userID": 12,
    "title": "My new post",
    "body": "body for my post TestPostTestPost",
})
print(response.status_code)
print(response.text)