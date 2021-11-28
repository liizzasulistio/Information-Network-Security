import hashlib

h = hashlib.sha3_256()

data = "Hello World!"
print("Input : ", data)
h.update(data.encode('utf-8'))
st = ""
for i in h.digest():
    st += str(hex(i)) + "/"
print(st)

#h.update(b"tambah string lagi")
#for i in h.digest():
#    st += str(hex(i)) + "/"
#print(st)
