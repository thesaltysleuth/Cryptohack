from pwn import * # pip install pwntools
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')



def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



for iter in range(0,101):

	flag=""

	received = json_recv()
	print("level : "+ str(iter))

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	if(received["type"]=="base64"):
		val=b64d("{}".format(received["encoded"])).decode('utf-8')
	if(received["type"]=="hex"):
		val=bytes.fromhex(received["encoded"]).decode('utf-8')
	if(received["type"]=="rot13"):
		val=codecs.decode("{}".format(received["encoded"]),'rot_13')
	if(received["type"]=="bigint"):
		val=bytes.fromhex("{}".format(received["encoded"])[2:]).decode('utf-8')
	if(received["type"]=="utf-8"):
		for i in received["encoded"]:
			flag+=chr(i)
		val=flag
	to_send = {
	    "decoded": val
	}


	json_send(to_send)



