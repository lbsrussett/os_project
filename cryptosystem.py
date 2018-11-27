import rsa
import person
import sys
import txt_to_decimal as td
from time import sleep
import random
import math

# class Cryptosystem:

#randomly selects a prime from a premade list
def getPrime():
    p = [88087912304403812848099579267617802897444475375227478742367042418362692676847519578296269543872388788102059936339296956631750606731090389119815333686208151,
         24127874376746971470740723338118723069434823629601370713879229211620985383174378400175905580937219786248135237339357716161802609654002549152864172290129173,
         10017086802729983535241005506999524261839846718045826210061198758360490652927154502193076067437830832391074104138019648396382232234276326584062853663824591,
         92548489982746270461293213385257818608232903205046073452860710066254812932995111743858431578584151456083297019349400072746090661865278459156792473130432657]
    
    q = [86280211721696198293503837466457902681823706168531007035193232822190725124132480598394061875954304751984590467299576173479100910197423628632415914698477359,
         31170216324807436590964148240105308432254052810827520941064360667525083130436529987693614217886447300690892098722255674460940412985044372591141649738656779,
         97628883804682209030932040526168709122285053007464228553430518105812350050124288409464913261796826696031057632664039281518902962031332857616573493917391683,
         14489849018226410329632873754284731121736068882169755057642460409642191993652630102433042282001520578040778206021826411972055131742967190759161400625460273]
    
    r = random.randrange(1,4)
    t = random.randrange(1,4)
    
    return p[r], q[t]
#check if a number is prime or not, takes a long time for big numbers
def isPrime(n):
    print("/t", n)
    if n > 1:
        for i in range(2,n):
            print(i)
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
#generates random prime, but takes a long time
def genPrime(k):
    r=100*(math.log(k,2)+1)
    print(r)
    r_ = r
    while r>0:
        print(r)
        n = random.randrange(2**(k-1),2**(k))
        r-=1
        if isPrime(n) == True:
            return (n)
    return getBackupPrime


if __name__ == "__main__":
    # convert text to an integer
    p, q = getPrime()
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
    
    input("Press Enter to continue...\n")
    
    #=======================================
    #   Calculate Keys
    #=======================================
    p1 = person.Person('Alice',p,q)
    p2 = person.Person('Bob',p, q)
    #pow(2,31) - 1,pow(2,61) - 1
    p1_pk, p1_sk = p1.set_keys()
    p2_pk, p2_sk = p2.set_keys()
    print("public key for " + p1.name + " : {}\n".format(p1.pk))
    sleep(0.5)
    print("private key for " + p1.name + " : {}\n".format(p1.sk))
    
    input("Press Enter to continue...\n")

    print("public key for " + p2.name + " : {}\n".format(p2.pk))
    sleep(0.5)
    print("private key for " + p2.name + " : {}\n".format(p2.sk))
    
    input("Press Enter to continue...\n")

    #===============================================
    #    Pass Public Keys
    #===============================================

    print("Alice sends Bob her public key: {}\n".format(p1.pk))
    sleep(0.5)
    print("Bob sends Alice his public key: {}\n".format(p2.pk))
    p2.other_pk = p1.pk
    p1.other_pk = p2.pk
    
    input("Press Enter to continue...\n")

    #================================================
    #     Encrypt Message
    #================================================
    text = messages[0].rstrip()
    print("Message to encrypt: {}".format(text))
    input("Press Enter to continue...\n")

    block_int = td.to_decimal(text)
    print("Block int created from the message text: {}\n".format(block_int))
    input("Press Enter to continue...\n")

    #encrypt the message
    cipher = p2.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p2.name + ": {}\n".format(cipher))
    input("Press Enter to continue...\n")

    #====================================================
    #     Decrypt Message
    #====================================================
    #decrypt the message
    block_int = p1.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    input("Press Enter to continue...\n")

    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p1.name + ": {}\n".format(txt))

    input("Press Enter to continue...\n")
    #======================================================
    #    Second Message
    #======================================================
    sleep(0.5)
    text = messages[1].rstrip()
    print("Message to encrypt: {}\n".format(text))
    sleep(0.5)
    block_int = td.to_decimal(text)
    print("Block int created from the message text: {}\n".format(block_int))
    input("Press Enter to continue...\n")

    #encrypt the message
    cipher = p1.send_message(block_int)
    sleep(0.5)
    print("Encrypted cipher for " + p1.name + ": {}\n".format(cipher))
    input("Press Enter to continue...\n")

    #decrypt the message
    block_int = p2.receive_message(cipher)
    sleep(0.5)
    print("Decrypted int from cipher: {}\n".format(block_int))
    input("Press Enter to continue...\n")

    #convert int to string
    txt = td.to_string(block_int, len(text))
    sleep(0.5)
    print("Decrypted text for " + p2.name + ": {}\n".format(txt))

    # sleep(0.5)
    # text = messages[2].rstrip()
    # print("Message to encrypt: {}\n".format(text))
    # sleep(0.5)
    # block_int = td.to_decimal(text)
    # print("Block int created from message text: {}\n".format(block_int))
    # #encrypt the message
    # cipher = p2.send_message(block_int)
    # sleep(0.5)
    # print("Encrypted cipher for " + p2.name + ": {}\n".format(cipher))
    # #decrypt the message
    # block_int = p1.receive_message(cipher)
    # sleep(0.5)
    # print("Decrypted int from cipher: {}\n".format(block_int))
    # #convert int to string
    # txt = td.to_string(block_int, len(text))
    # sleep(0.5)
    # print("Decrypted text for " + p1.name + ": {}\n".format(txt))

    # sleep(0.5)
    # text = messages[3].rstrip()
    # print("Message to encrypt: {}\n".format(text))
    # sleep(0.5)
    # block_int = td.to_decimal(text)
    # print("Block int creted from message text: {}\n".format(block_int))
    # #encrypt the message
    # cipher = p1.send_message(block_int)
    # sleep(0.5)
    # print("Encrypted cipher for " + p1.name + ": {}\n".format(cipher))
    # #decrypt the message
    # block_int = p2.receive_message(cipher)
    # sleep(0.5)
    # print("Decrypted int from cipher: {}\n".format(block_int))
    # #convert int to string
    # txt = td.to_string(block_int, len(text))
    # sleep(0.5)
    # print("Decrypted text for " + p2.name + ": {}\n".format(txt))
    
    
    

    

   
