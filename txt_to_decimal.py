SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def to_decimal(text):
    ls = len(SYMBOLS)
    block_int = SYMBOLS.index(text[0]) * (ls ** 0)
    for i in range(1, len(text)):
        block_int += SYMBOLS.index(text[i]) * (ls ** i)

    return block_int

def to_string(in_int, msg_len):
    msg = []
    for i in reversed(range(msg_len)):
        msg.append(SYMBOLS[in_int // len(SYMBOLS) ** i])
        in_int = in_int % (len(SYMBOLS) ** i) 

    msg = ''.join(i for i in reversed(msg))
    return msg 

if __name__ == "__main__":
    txt = 'hello !'
    block = to_decimal(txt)
    print(block)
    txt = to_string(block, 7)
    print(txt)
