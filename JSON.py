import json

data = {

    "to_user": "sergey",
    "text": "hello",
    "attachments": ['1.png', '2.wav'],
    "type": "direct",
    "demolition": None,

}

json_str = json.dumps(data) #from py_obj to json_str
print(json_str)
print(type(json_str))

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)

        return o

json_str1 = json.dumps({1, 2, 3}, cls=MyEncoder) #from py_obj to json_str
print(json_str1)



py_obj = json.loads(json_str)
print(py_obj['to_user'])

print(json.loads(json_str))