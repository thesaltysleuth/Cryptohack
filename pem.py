from Crypto.PublicKey.RSA import import_key


f=open('/root/Downloads/keypair_1f696c053d76a78c2c531bb013a92d4a.pem','r')

contents=f.read()

key=import_key(contents)

print(int(key.d))