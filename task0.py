def fizzbuzz():
    for i in range(101):
        if i == 0:
            print(i)
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()