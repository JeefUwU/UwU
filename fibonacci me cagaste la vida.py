def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
num=int(input("ingrese cuentos numeros quiere considerar: "))
for i in range(num+1):
    print(rec_fib(i))