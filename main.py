import rsa 
import txt_to_decimal as td


if __name__ == "__main__":
    # convert text to an integer
    txt = "attack at dawn"
    print("Message to encrypt: {}".format(txt))
    block_int = td.to_decimal(txt)
    print("Block int: {}".format(block_int))

    # create the keys
    rsa = rsa.RSA(pow(2,31) - 1, pow(2,61) - 1)
    pk, sk = rsa.calc_keys()
    print("public key: {}".format(pk))
    print("private key: {}".format(sk))

    # encrypt the message 
    cipher = rsa.encrypt(block_int, pk)
    print('cipher: {}'.format(cipher))

    # decrypt the message
    block_int = rsa.decrypt(cipher, sk)
    print("decrypt int: {}".format(block_int))

    # convert int to string 
    txt = td.to_string(block_int, len(txt))
    print("Decrypted txt: {}".format(txt))
