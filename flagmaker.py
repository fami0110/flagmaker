import sys
import os

def cipher(flag, prefix="CTF", signature = False):
    lookup = [
        ['O', 'o'],
        ['I', 'l'],
        ['R', 'z'],
        ['E', 'e'],
        ['A', 'a'],
        ['S', 's'],
        ['G', 'b'],
        ['T', 't'],
        ['B'],
        ['g']
    ]

    flag = flag.replace(' ', '_')
    
    for index, i in enumerate(lookup):
        for j in i:
            flag = flag.replace(j, str(index))

    if signature:
        flag = f"{flag}_{bytes.hex(os.urandom(3))}"

    return prefix + "{" + flag + "}"


def main(args):
    signature = False
    prefix = "CTF"
    plain = None

    for i in range(len(args)):
        if args[i] == '-t' and plain == None:
            i += 1
            plain = args[i]
        elif args[i] == '-p':
            i += 1
            prefix = args[i]
        elif args[i] == '-s':
            signature = True
        else:
            i += 1

    if (".txt" in plain):
        res = ""
        for line in open(plain, 'r').readlines():
            res += cipher(line.strip(), prefix, signature) + "\n" 
        open('output.txt', 'w').write(res)
        print(plain, "===> output.txt")
    else:
        print(cipher(plain, prefix, signature))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python flagmaker.py -t [plaintext/dictionary.txt] -p [prefix] [-s (random signature: optional)]')
        sys.exit(1)
    else:
        main(sys.argv[1:])