tal = int(input("Enter a positiv odd number: "))

if tal%2 == 0 or tal < 0:
    print("Disallowed number entered.")

else:
    while tal >= 1:
        print("*" * tal)
        tal = tal - 1