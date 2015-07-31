while True:
    r = input("Please enter a number:")
    if r.isalpha():
        print("ERROR: Not a number.")
    elif (not r.isdigit()):
        print ("ERROR: Not a positive integer.")
    else:
        break

number = int(r)

def factors(number):
    if number == 1:
        return []

    for i in range(2, number):
        rd, qt = divmod(number, i)
        if not qt:
            return [i] + factors(rd)

    return [number]

print (factors(number))