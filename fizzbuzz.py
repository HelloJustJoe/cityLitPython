def fizzbuzz(num):
    for x in range(num+1):
        if (x % 3 == 0 and x % 5 == 0):
            print(f"{x} FizzBuzz")
        elif (x % 3 == 0):
            print(f"{x} Fizz")
        elif (x % 5 == 0):
            print(f"{x} Buzz")
        else:
            print(x)


fizzbuzz(100)