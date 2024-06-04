import random
import re

def generate_password(email):
    username = re.findall(r'[a-zA-Z0-9]+(?=@)', email)[0]
    password = ''.join(chr(random.randint(33, 126)) for _ in range(8))
    return f'{email} username: {username} , password: {password}'
emails = ['doal@mail.com', 'ciss@gmail.co.id', 'jiii@jar.com', 'lah@pen.com']
for email in emails:
    print(generate_password(email))