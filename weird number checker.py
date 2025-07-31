# Read an integer from input
n = int(input("enter number: "))

# Check conditions based on problem rules
if n % 2 != 0:
    print("Weird")  # Odd numbers are always "Weird"
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")  # Even numbers greater than 20 are "Not Weird"
