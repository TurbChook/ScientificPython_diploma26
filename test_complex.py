from module import complex
def main():
    a = complex(10,15)
    b = complex(2,5)
    print(a)
    print(b)
    print(f"Sum:{a+b}")
    print(f"Subs:{a-b}")
    print(f"Mul{a*b}")
    print(f"Division:{a/b}")
    print(f"Mod:{a.modulus()}")
if __name__ == "__main__":
    main()
