import rsa
import person
import sys
import txt_to_decimal as td
from time import sleep

# class Cryptosystem:


if __name__ == "__main__":
    # convert text to an integer
    p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
    q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
    with open('input.txt', 'r') as f:
    	content = f.readlines()
    	messages = []
    	for c in content:
    		messages.append(c)

    # txt = messages[0].rstrip()
    # print("Message to encrypt: {}".format(txt))
    # block_int = td.to_decimal(txt)
    # print("Block int: {}".format(block_int))
    print("Alice wants to communicate with Bob securely.\n")
    print("Bob and Alice both calculate their public and secret keys.\n")
    sleep(0.5)

    p1 = person.Person('Alice',p,q)
    p2 = person.Person('Bob',p, q)
    #pow(2,31) - 1,pow(2,61) - 1
    p1_pk, p1_sk = p1.set_keys()
    p2_pk, p2_sk = p2.set_keys()
    print("public key for " + p1.name + " : {}\n".format(p1.pk))
    sleep(0.5)
    print("private key for " + p1.name + " : {}\n".format(p1.sk))
    sleep(0.5)

    print("public key for " + p2.name + " : {}\n".format(p2.pk))
    sleep(0.5)
    print("private key for " + p2.name + " : {}\n".format(p2.sk))
    sleep(0.5)

    print("Alice sends Bob her public key: {}\n".format(p1.pk))
    sleep(0.5)
    print("Bob sends Alice his public key: {}\n".format(p2.pk))
    p2.other_pk = p1.pk
    p1.other_pk = p2.pk
    sleep(0.5)

    text = messages[0].rstrip()
    print("Message to encrypt: {}".format(text))
    sleep(0.5)
    block_int = td.to_decimal(text)
    print("Block int created from the message text: {}\n".format(block_int))
    #encrypt the message
    cipher = p2.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p2.name + ": {}\n".format(cipher))
    #decrypt the message
    block_int = p1.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p1.name + ": {}\n".format(txt))

    sleep(0.5)
    text = messages[1].rstrip()
    print("Message to encrypt: {}\n".format(text))
    sleep(0.5)
    block_int = td.to_decimal(text)
    print("Block int created from the message text: {}\n".format(block_int))
    #encrypt the message
    cipher = p1.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p1.name + ": {}\n".format(cipher))
    #decrypt the message
    block_int = p2.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p2.name + ": {}\n".format(txt))

    sleep(0.5)
    text = messages[2].rstrip()
    print("Message to encrypt: {}\n".format(text))
    sleep(0.5)
    block_int = td.to_decimal(text)
    print("Block int created from message text: {}\n".format(block_int))
    #encrypt the message
    cipher = p2.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p2.name + ": {}\n".format(cipher))
    #decrypt the message
    block_int = p1.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p1.name + ": {}\n".format(txt))

    sleep(0.5)
    text = messages[3].rstrip()
    print("Message to encrypt: {}\n".format(text))
    sleep(0.5)
    block_int = td.to_decimal(text)
    print("Block int creted from message text: {}\n".format(block_int))
    #encrypt the message
    cipher = p1.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p1.name + ": {}\n".format(cipher))
    #decrypt the message
    block_int = p2.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p2.name + ": {}\n".format(txt))
    
    
    

    

   