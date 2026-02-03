a = 20
def main():
    a = 10
    print(a, globals()['a'], end ="")
    print(globals()['a'])
main()
