a = 0
for i in range(100):
    a = a+1
    if a%3 == 0 and a%5 ==0:
        print("fizzbuzz")
    elif a%3 == 0:
        print("fizz")
    elif a%5 == 0:
        print("buzz")
    else:
        print(a)
