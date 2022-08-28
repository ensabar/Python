import json
## Deserialization
#person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles":["engineer", "programmer"]}
#
## Convert to a json object
#personJSON = json.dumps(person, indent=4, sort_keys=True)
##print(personJSON)
#
##with open('json/person.json', 'w') as file:
##    json.dump(person, file, indent=4)
#
#
## Decoding
#with open('json/person.json', 'r') as file:
#    person = json.load(file)
#    print(person)
###########################################################


class User:

    def __init__(self, name, age):
         self.name = name
         self.age = age

user = User('Max', 27)

# Custom enconding function

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

# Custom JSON Encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

#userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

# Decode JSON

# CUstom decode method
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)


