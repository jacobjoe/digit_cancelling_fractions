""" Digit cancelling fraction """
# heading for user understanding
print("Two Digit cancelling fraction")
# try block for if user gives input as numbers
try:
    n = int(input("Enter numerator number :"))
    d = int(input("Enter denominator number :"))
    num = []
    den = []
    for i in str(n):
        num.append(int(i))
    for j in str(d):
        den.append(int(j))
    numerator = 0
    denominator = 0
    # if num's first value not in den this if condition execute
    if num[0] not in den:
        # if num's second value also not in den this conditioin execute
        if num[1] not in den:
            numerator += num[0]
            numerator = numerator * 10 + num[1]
            denominator += den[0]
            denominator = denominator * 10 + den[1]
        else:
            if num[1] == den[0]:
                num.remove(num[1])
                den.remove(den[0])
                numerator += num[0]
                denominator += den[0]
            elif num[1] == den[1]:
                num.remove(num[1])
                den.remove(den[1])
                numerator += num[0]
                denominator += den[0]
    # elif condition if num's first value in den
    elif num[0] in den:
        # if condition for if num and den have same numbers
        if num[0] == den[0] and num[1] == den[1] or num[1] == den[0] and num[0] == den[1]:
            print("Numerator and denominators have same numbers")
        # elif for check whether num's first is in den's first num
        elif num[0] == den[0]:
            num.remove(num[0])
            den.remove(den[0])
            numerator += num[0]
            denominator += den[0]
        # elif for check whether num's first is in den's second num
        elif num[0] == den[1]:
            num.remove(num[0])
            den.remove(den[1])
            numerator += num[0]
            denominator += den[0]

    print(numerator, '/', denominator)

# exception for if user gives input as letters
except ValueError:
    print("Your input is not numerical value")
