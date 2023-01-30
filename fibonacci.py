def fibonacci(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        for i in range (2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
        
n = 20
print ("Fibonacci series up to", n, "terms", fibonacci(n))