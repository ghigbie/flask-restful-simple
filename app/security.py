from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'Bob', 'asdf'),
    User(2, 'Kat', 'abcd'),
    User(3, 'Nat', 'abcd'),
    User(4, 'Aiko', 'abcd'),
    User(5, 'Super', 'abcd')
]

username_mapping = {u.username: u for u in users} #creates dictionary of usersnames with info
userid_mapping = {u.id: u for u in users} # creates dictionary of id with info

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)