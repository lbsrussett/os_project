import rsa
import person
import sys
import txt_to_decimal as td

# class Cryptosystem:


if __name__ == "__main__":
    # convert text to an integer

    with open('input.txt', 'r') as f:
    	content = f.readlines()
    	messages = []
    	for c in content:
    		messages.append(c)

    txt = messages[0].rstrip()
    print("Message to encrypt: {}".format(txt))
    block_int = td.to_decimal(txt)
    print("Block int: {}".format(block_int))
    p1 = person.Person('Alice',pow(2,31) - 1,pow(2,61) - 1)
    p2 = person.Person('Bob',307, 653)
    
    p1_pk, p1_sk = p1.set_keys()
    p2_pk, p2_sk = p2.set_keys()
    print("public key for " + p1.name + " : {}".format(p1.pk))
    print("private key for " + p1.name + " : {}".format(p1.sk))

    print("public key for " + p2.name + " : {}".format(p2.pk))
    print("private key for " + p2.name + " : {}".format(p2.sk))

    # encrypt the message 
    cipher = p1.send_message(block_int)
    print("cipher for " + p1.name + ": {}".format(cipher))

    # decrypt the message
    block_int = p1.receive_message(cipher)
    print("decrypt int: {}".format(block_int))

    # convert int to string 
    txt = td.to_string(block_int, len(txt))
    print("Decrypted txt: {}".format(txt))

   