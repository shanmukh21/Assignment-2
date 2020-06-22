from Crypto.Cipher import DES
import string
cnt = 0
ciphertext = "4B518774A408E3E5"
s = string.letters + string.digits
for i in range(255):
    for j in range(255):
        for k in range(255):
            for l in range(255):
                for m in range(255):
                    for n in range(255):
                        for o in range(255):
                            for p in range(255):
                                skey = chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n)+chr(o)+chr(p)
                                des = DES.new(skey,DES.MODE_ECB)
                                plaintext = des.decrypt(ciphertext.decode("hex"))
                                if(all(a in s for a in plaintext)):
                                    print cnt
                                    print(plaintext)
                                    f  = open('plaintext',"s")
                                    f.write("[ " + skey.encode("hex") + " : ")
                                    f.write(plaintext + " ]\n")
                                    f.close()
                                cnt += 1
