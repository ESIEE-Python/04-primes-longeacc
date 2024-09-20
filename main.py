"""cette  fonction test si le nombre choisi est premier ou non"""
def isprime(p):
    """cette  fonction test si le nombre choisi est premier ou non"""
    if p < 2:
        return False
    for n in range(2, p):
        if p % n == 0:
            return False
    return True
def main():
    """cette  fonction test si le nombre choisi est premier ou non"""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
