import hashlib, sys, os


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
 █▀▄▀█ █▀▄ █▀
 █░▀░█ █▄▀ ▄█  V 1.0.0
 
 █░█ ▄▀█ █▀ █░█   █▄▄ █▀▀
 █▀█ █▀█ ▄█ █▀█   █▄█ █▀░

 Coder By : https://github.com/Nux-xader
 Contact  : https://wa.me/6281251389915
 _________________________________________
""")


def main():
    clr()
    banner()
    while True:
        path = str(input(" [*] Word list path : "))
        try:
            wordlist = [i for i in str(open(path, "r").read()).split("\n") if len(i) > 0]
            break
        except:
            print(f" [!] File {path} not found")

    hashed = str(input(" [*] Input hash : "))
    clr()
    banner()
    for word in wordlist:
        hashes = hashlib.md5(word.encode('utf-8')).hexdigest()
        if hashed == hashes:
            print(f" [+] Valid hash >> [{word}]")
            break
        print(f" [-] Inalid hash >> [{word}]")
        
    else:
        print(f" [!] Can't find Valid hash on {path}")




if __name__ == "__main__":
    main()