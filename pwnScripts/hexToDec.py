from pwn import *
import base64

r = remote('127.0.0.1', 11111)

data = r.recv()
count = 0

while data.find('prize') == -1:
    print data
    count += 1
    response = base64.b64decode(data)
    response = response.split('==')[0]
    
    print str(count) 
    print response
    r.send(response + '\n')
    data = r.recv()

print data
data = r.recv()
print data
