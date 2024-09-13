from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p < 2:
        print("Ce n'est pas un nombre premier")
        return False

    for n in range(2, p):
        if p % n == 0:
            print("Ce n'est pas un nombre premier")
            return False

    print("C'est un nombre premier")
    return True

#### Fonction principale


def main():
    try:
        p = int(input("Choisis un nombre: "))
        if isprime(p):
            print(f"{p} est un nombre premier.")
        else:
            print(f"{p} n'est pas un nombre premier.")
    except ValueError:
        print("Ce n'est pas un nombre valide.")


    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
