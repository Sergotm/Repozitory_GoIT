

def lar_a():
    import module_b
    # module_b.lar_b()
    print('function lar_a from module a')
    module_b.lar_b()


if __name__ == '__main__':
    lar_a()
