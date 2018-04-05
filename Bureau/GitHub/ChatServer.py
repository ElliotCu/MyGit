import socket 
import threading
import select


HOST = ''
PORT = 7777
tick = time.asctime((time.localtime(time.time())))


server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
print ("Socket created")

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

##Bind socket to local host and port
server_socket.bind((HOST, PORT))
print ("Socket bind complete\n")


server_socket.listen(5)
#Empty Socket list
socket_list = []
#Empty ip list
ip_list = {}

while True:
	ready_to_read, ready_to_write, in_error = select.select(socket_list+[server_socket], [], [])
	for sock in ready_to_read:
		if sock == server_socket:
			server_socket_2 = server_socket.accpet()
			ip_list[server_socket_2[0]] = server_socket_2[1][0]
			socket_list.append(server_socket_2[0])
			Notify = str(server_socket_2[1][0] + "Entered The Chat room\n")
			for i in socket_list:
				i.send(bytes(Notify,"utf-8"))
		else:
			MSG = sock.recv(4096)
			if (len(MSG) == 0):
				Notify = str(ip_list[i]+"Left The Chat Room!\n")
				for i in socket_list:
					i.send(bytes(Notify,"utf-8"))
				socket_list.remove(i)
				i.close()
				del ip_list[i]
				






# def broadcast (server_socket, sock, MSG):
#     for socket in socket_list:
#         # send the message only to peer
#         if socket != server_socket and socket != sock :
#             try :
#                 socket.send(MSG)
#             except :
#                 # broken socket connection
#                 socket.close()
#                 # broken socket, remove it
#                 if socket in SOCKET_LIST:
#                     socket_list.remove(socket)


# def JOIN(socket_server):
#     ready_to_read, ready_to_write, in_error = select.select(socket_list+[server_socket], [], [])
#     for sock in ready_to_read:
#         if sock == server_socket:
#             conn, addr = server_socket.accpet()
#             socket_list.append(conn)
#             print("Client (%s, %s) connected % addr")
#             broadcast(server_socket, conn, "[%s:%s] entered our chatting room\n" % addr)

# def PART(socket_server):
#     ready_to_read, ready_to_write, in_error = select.select(socket_list+[server_socket], [], [])
#     for sock in ready_to_read:
#         if sock == server_socket:
#             data = conn.recv(4096)
#             d = data.send(data)
#             if (d == 0):
#                 print("Client (%s, %s) disconnected % addr")
#                 broadcast(server_socket, conn, "[%s:%s] left our chatting room\n" % addr)

# def NICK(new_socket_server):
#     nick_dict = {}
#     if JOIN :
#         conn, addr = server_socket.accept()
#         socket_list.append(conn)
#         nick_dict ['conn'] = ['new_socket_server']

