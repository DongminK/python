import socket

from insoft.openmanager.message.agent_packet import AgentPacket
from insoft.openmanager.message.message import Message
from insoft.openmanager.message.packet import Packet
from insoft.openmanager.message.packet_writer import PacketWriter

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("192.168.255.79", 10000)

sock.bind(server_addr)
sock.listen()

while True:
	print("Waiting client...")
	connection, client_addr = sock.accept()
	try:
		print("Connected.. ", client_addr)

		packet = AgentPacket()
		msg = packet.recv(connection)
		print("[REQ]")
		print(msg)

		send_data = PacketWriter().parse_to_bytes(msg)
		packet.send(connection, send_data)


	except Exception as e:
		print(e)







