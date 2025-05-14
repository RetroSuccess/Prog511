import math


while True:
    try:
        x = float(input("Enter a number for x (-1 < x < 1): "))
        if -1 < x < 1:
            break
        else:
            print("Enter a proper number: ")
    except ValueError:
        print("Please enter proper number: ")

print("Choose a way to stop: ")
print("1: stops when the difference between them is less than this")
print("2: Maximum number of terms")

while True:
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        precision = float(input("Enter precision eg. (0.000001): "))
        max_terms = None
        break
    elif choice == "2":
        max_terms = input("Ener number of terms: ")
        precision = None
    else:
        print("Invalid choice. Enter 1 or 2: ")

current_sum = 0
previous_sum = 0
term_count = 0
exact_val = math.log(1 + x)


print("\nCalculation progress:")
print(f"{'Term':<5} {'Value':<15} {'Running Total':<15} {'Difference':<15}")

# Calculate the series
while True:
    term_count += 1
    term = ((-1) ** (term_count + 1)) * (x ** term_count) / term_count
    previous_sum = current_sum
    current_sum += term

    # Print progress
    difference = current_sum - previous_sum
    print(f"{term_count:<5} {term:<15.10f} {current_sum:<15.10f} {abs(difference):<15.10f}")

    # Check stopping conditions
    if precision is not None and abs(difference) < precision:
        break
    if max_terms is not None and term_count >= max_terms:
        break

# Print summary
print("\nSummary:")
print(f"Final approximation: {current_sum:.10f}")
print(f"Exact value (math.log): {exact_val:.10f}")
print(f"Number of terms used: {term_count}")
print(f"Difference: {abs(current_sum - exact_val):.10f}")


