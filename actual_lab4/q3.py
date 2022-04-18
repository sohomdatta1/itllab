class Pow:
    def pow(x,n):
        if x == 1:
            return 1
        if x == 0:
            return 0
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n < 0:
            val = 1
            for i in range(0, n * -1):
                val = val * 1/x
            return val
        elif n == 0:
            return 1
        else:
            val = 1
            for i in range(0, n):
                val = val * x
            return val
a =  int(input('Enter a number: '))
b = int(input('Enter power: '))
print(Pow.pow(a, b))
