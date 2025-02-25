with open('models.py', 'rb') as f:
    content=f.read().replace(b'\x00',b'')

with open('models.py', 'wb') as f:
    f.write(content)