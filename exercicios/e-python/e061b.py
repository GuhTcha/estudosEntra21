def ela_mesma(n):
    print(':',n)
    if n<= 1:
        return n
    else:
        ret = ela_mesma(n-1) + ela_mesma(n-2)
        return ret

num = int(input('Digite um número:'))
x = ela_mesma(num-1)
print('fim:',x)
# x=ela_mesma(8)
# print(x)