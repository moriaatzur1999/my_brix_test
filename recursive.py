
def my_super_digit(n, k, sp):
    if n <= 0 and (sp >= 10 or sp*k >= 10):
        n = sp * k
        k = 1
        sp = 0
    if n <= 0 and sp < 10 :
        return sp * k
    sp = sp + n%10
    return my_super_digit(n//10, k, sp)

def super_digit(n, k):
    return my_super_digit(n, k, 0)

if __name__ == '__main__':
    print(super_digit(123, 3))

