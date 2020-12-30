def Fizz_Buzz(numbers):

    for n in numbers:
        if n % 3 == 0 and n % 5 == 0: print('FizzBuzz')
        elif n % 5 == 0: print('Buzz')
        elif n % 3 == 0: print('Fizz')
        else: print(n)

number = list(range(100))

Fizz_Buzz(number)