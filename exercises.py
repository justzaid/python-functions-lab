# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base, height):
    return (base * height) / 2


print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))

print("===================================")

# Exercise 2: Calculate Simple Interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))
print('Exercise 2:', simple_interest(1500, 3.5, 5))

print("===================================")

# Exercise 3: Apply a Discount

def apply_discount(price, percentage):
    return int(price - price * percentage / 100)

print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))

# Exercise 4: Convert Temperature

def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature -32) * 5/9

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

print("===================================")

# Exercise 5: Sum to N

def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))
print('Exercise 5:', sum_to(10))

print("===================================")

# Exercise 6: Find the Largest Number

def largest(*args):
    return max(*args)


print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 2, 3))

print("===================================")

# Exercise 7: Calculate a Tip

def calculate_tip(bill, tip):
    return int(bill * tip / 100)

print('Exercise 7:', calculate_tip(50, 20))

print("===================================")

# Exercise 8: Calculate Product of Numbers

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8:', product(-1, 4))
print('Exercise 8:', product(2, 5, 5))

print("===================================")

# Exercise 9: Basic Calculator

def basicCalculator(num1, num2, kwargs):
    if kwargs == "add":
       return num1 + num2
    elif kwargs == "subtract":
       return num1 - num2
    elif kwargs == "multiply":
       return num1 * num2
    elif kwargs == "divide":
       return num1 / num2

print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))
print('Exercise 9 Result:', basicCalculator(10, 5, "add"))
print('Exercise 9 Result:', basicCalculator(10, 5, "multiply"))
print('Exercise 9 Result:', basicCalculator(10, 5, "divide"))