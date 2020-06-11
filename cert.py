from Crypto.PublicKey.RSA import import_key


f=open('/root/Downloads/2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der','rb')

contents=f.read()

key=import_key(contents)

print(key.n)
