def fibonachi(n):
    if n <= 1:
        return n
    else:
        result = fibonachi(n-1)+(n-2)
        print(f'{result}')
        return result
    
print(fibonachi(20))