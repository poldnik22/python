"""

HTTP

"""
import requests

#requests - мы делаем на сервер как клиент
#response - мы получаем от сервера.

page = requests.get("http://google.com")
print(page)

#200 - Ok
#404 - запрашиваемый ресурс не найден
#500 - внутренняя ошибка на сервере.

page = requests.get("http://google.com")
print(page.status_code)

#типовая ситуация. Если возврщаем 200 то выполняем все, если нет то другие инструкции

if page.status_code == 200:
    print("Ok")
else:
    print("Error", page.status_code)

#получим page content в виде строк байт
if page.status_code == 200:
    print(page.content)
else:
    print("Error", page.status_code)

# получим контент страницы и декодируем его в обычную строку, но довольно большая
if page.status_code == 200:
    print(page.content.decode("utf-8"))
else:
    print("Error", page.status_code)

# если мы не знаем кодировку и надо раскодировать, то можем раскодировать ту кодировку, которая пришла от сервера.
if page.status_code == 200:
    print(page.content.decode(page.encoding))
else:
    print("Error", page.status_code)

# если мы не знаем кодировку и надо раскодировать, то можем раскодировать ту кодировку, которая пришла от сервера.
if page.status_code == 200:
    print(page.text)
else:
    print("Error", page.status_code)

# как предоставлять данные в наш URL
print("_________________________________________________________________________________")

page2 = requests.get("http://google.com", params={
    "q": "cats dogs pigs"
})

if page2.status_code == 200:
    print(page2.url)
else:
    print("Error", page2.status_code)

print("_________________________________________________________________________________")
print(page2.headers)
print(page2.headers['Content-Type'])

#как работать с json
print("_________________________________________________________________________________")
page3=requests.get("https://jsonplaceholder.typicode.com/post") #сайт позволяющий работать с фейковым rest api
print(page3.headers)
print(page3.headers['Content-Type'])