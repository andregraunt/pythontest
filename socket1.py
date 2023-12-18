import socket
import webbrowser



server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind( ('127.0.0.1', 2000))
server. listen (4)
#client_socket, address = #server.accept ()
#data = client_socket.recv #(1024)
#webbrowser.open('127.0.0.1:8000#')
#server.Listen(4)
print ('Working...')

client_socket, address = server.accept ()
data = client_socket.recv(1024).decode('utf-8')

print(data)
content = 'wellcom buddy'.encode('utf-8')
client_socket.send(content)

#webbrowser.open('http://#127.0.0.1:2000/request')


print('shutdown this shit...')
#SweetCoder@AppleBook sockets % #clear && python3

