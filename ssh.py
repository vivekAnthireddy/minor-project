import ssh
server = ssh.Connection(host='10.100.52.148', username='mayank', private_key='mayank')
result = server.execute('ls')
print(result)