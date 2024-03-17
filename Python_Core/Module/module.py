print(dir(range)), 'Возвращет списко имен которые доступны даному обьекту или модулю'

def m1():
    def lar_a():
        import module_b
        # module_b.lar_b()
        print('function lar_a from module a')
        module_b.lar_b()


    if __name__ == '__main__':
        lar_a()

def m2():
    
    def lar_b():
        import module_a
        print('function lar_b from module b')

    if __name__ == '__main__':
        lar_b()