import MathLibrary

options = int(input("Please select and input from 1-XX: "))
while options != -1:
    if options == 1:
        print("Find the factorial of a selected number.")
        n = int(input("Enter a number (n): "))
        print("The value of", n, "! is:", MathLibrary.factorial(n))
        options = int(input("Please select and input from 1-XX: "))

    if options == 2:
        print("This function will let you find the natural log (ln) of any number.")
        x = float(input("Enter a number (x): "))
        print("The value of ln(", x, ") is:", MathLibrary.naturalLog(x))
        options = int(input("Please select and input from 1-XX: "))

    if options == 3:
        print("This function will let you find the power of any  2 numbers.")
        a = float(input("Enter a number (a) for the base: "))
        x = float(input("Enter a number (x) for the exponent: "))
        print("The value of ", a, "^", x, " is: ", MathLibrary.powers(a, x))
        options = int(input("Please select and input from 1-XX: "))

    if options == 4:
        print("This the nth number in the Fibonacci series.")
        n = int(input("Enter a an index of the series (n): "))
        print("The ", n, "th value of the Fibonacci series is: ", int(MathLibrary.fibonacci(n)))
        options = int(input("Please select and input from 1-XX: "))

    if options == 5:
        print("This function lists all the constants in this math library.")
        print("The value of Euler's Number (e) is: ", MathLibrary.eulersNumber())
        print("The value of pi (pi) is: ", MathLibrary.pinumber())
        print("The value of the Golden Ratio (phi) is: ", MathLibrary.goldenRatio())
        options = int(input("Please select and input from 1-XX: "))

    if options == 6:
        print("This function will let you find the logarithim with any base.")
        b = float(input("Enter a number (b) for the base: "))
        x = float(input("Enter a number (x) for the exponent: "))
        print("The value of log", b, "(", x, ") is: ", MathLibrary.logarithims(b, x))
        options = int(input("Please select and input from 1-XX: "))

    if options == 7:
        print("This function will let you find the number of permutations")
        n = float(input("Enter a number (n) for the total number of objects: "))
        r = float(input("Enter a number (r) number of objects to be selected: "))
        print("The value of ", int(n), "P", int(r), " is: ", int(MathLibrary.permutations(n, r)))
        options = int(input("Please select and input from 1-XX: "))

    if options == 8:
        print("This function will let you find the number of combinations")
        n = float(input("Enter a number (n) for the total number of objects: "))
        r = float(input("Enter a number (r) number of objects to be selected: "))
        print("The value of ", int(n), "C", int(r), " is: ", int(MathLibrary.combinations(n, r)))
        options = int(input("Please select and input from 1-XX: "))

    if options == 9:
        print("This function will let you find the nth root of any 2 numbers.")
        a = float(input("Enter a number (a) for the index: "))
        x = float(input("Enter a number (x) for the radicand: "))
        print("The value of the ", a, "th root of ", x, " is approximately: ", MathLibrary.roots(a, x))
        options = int(input("Please select and input from 1-XX: "))

    if options == 10:
        print("The value of pi is:", MathLibrary.pinumber())
        options = int(input("Please select and input from 1-XX: "))

    if options == 11:
        MathLibrary.listFunctions()
        options = int(input("Please select and input from 1-XX: "))

    if options == 12:
        r = float(input("Enter a number (r) for the radius: "))
        MathLibrary.circleArea(r)
        options = int(input("Please select and input from 1-XX: "))
    if options == 13:
        print(MathLibrary.Sieve(n))
        options = int(input("Please select and input from 1-XX: "))
