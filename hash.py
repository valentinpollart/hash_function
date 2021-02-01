def hash_function(message):
    n = 16
    slices = [message[i:i+n] for i in range(0, len(message), n)]
    slices[-1] = slices[-1].ljust(n, '0')
    asciis = ["".join([str(ord(i)).rjust(4,'0') for i in s]) for s in slices]
    digest = int(asciis[0])
    for i in asciis[1:]:
        digest = digest ^ int(i)
    return hex(int(digest)).strip("0x")
