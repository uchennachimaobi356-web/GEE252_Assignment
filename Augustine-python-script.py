# Gem252 Basic Python Assignment
# File_name = Augustine-Phython-script.py
# Matric number = ENV2303973

# Problem 1
print('===== problem 1 =====')
city_name = "Lagos"
population = 15000000
cordinate = (6.5244, 3.3792)
is_capital = False

print('City:', city_name, 'type:', type(city_name))
print('City:', population, 'type:', type(population))
print('City:', cordinate, 'type:', type(cordinate))
print('City:', is_capital, 'type:', type(is_capital))

area = 1000
population_density = population/area
print(population_density)


# Problem 2
print('\n===== Problem 2 =====')
cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Port Harcourt"]
cities.append('Benin City')
print(cities)
cities.insert(2, 'Kaduna')
print(cities)
cities.remove('Kano')
print(cities)
print('The length of the List is', len(cities))
print('cities in alphabetical order', sorted(cities))
print('Every Second city', cities[::2])


# Problem 3, 
print("\n===== Problem 3 =====")
city_data = {
    "Lagos":{"population": 15000000, "region":"Southwest"},
    "Abuja":{"population": 3000000, "region":"North Central"},
    "Kano":{"population": 4000000, "region":"Northwest"}
}
# add new city
city_data["Enugu"]={"poulation": 722000, "region": "southeast"}
print(city_data)
# update lagos location
city_data["Lagos"]["population"] = 16000000
print(city_data)
# Print all city names
print("cities:", list(city_data.keys()))
# Print region of abuja
print("Region of Abuja:", city_data["Abuja"]["region"])
#Print total population
# total_population = sum(city_data["population"] for city in city_data.values())
# print("Total population:", total_population)


# ==========================================================
# Problem 4: Loops
print("\n=== Problem 4 ===")

# Part A: For Loops
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("Characters in PYTHON:")
for ch in "PYTHON":
    print(ch, end=" ")
print()

sum_1_100 = sum(range(1, 101))
print("Sum from 1 to 100:", sum_1_100)

# Part B: While Loop
print("\nCountdown from 10 to 1:")
n = 10
while n >= 1:
    print(n, end=" ")
    n -= 1
print()

num = 1001
while num % 17 != 0:
    num += 1
print("First number >1000 divisible by 17:", num)


# # ==========================================================
# # Problem 5: Conditional Statements
print("\n=== Problem 5 ===")

def classify_temperature(temp):
    if temp > 30:
        return "Hot"
    elif 20 <= temp <= 30:
        return "Warm"
    elif 10 <= temp <= 19:
        return "Cool"
    else:
        return "Cold"

for t in [35, 25, 15, 5]:
    print(f"Temperature {t}°C:", classify_temperature(t))


# ==========================================================
# Problem 6: Functions
print("\n=== Problem 6 ===")

# Part A
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance (0,0) to (3,4):", calculate_distance(0,0,3,4))

# Part B
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_user("John"))
print(greet_user("Mary", "Hi"))

# Part C
def analyze_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

nums = [10, 25, 30, 15, 40]
print("Analyze numbers:", analyze_numbers(nums))


# ==========================================================
# Problem 7: String Operations
print("\n=== Problem 7 ===")

location = "Lagos, Nigeria, West Africa"

print("Uppercase:", location.upper())
print("Split by comma:", location.split(","))
print("Contains 'Nigeria':", "Nigeria" in location)
print("Replace West Africa:", location.replace("West Africa", "Western Africa"))
print("Count of 'a':", location.lower().count("a"))


# # ==========================================================
# # Problem 8: File Operations
print("\n=== Problem 8 ===")

try:
    with open("cities.txt", "w") as f:
        f.write("Lagos,15000000\nAbuja,3000000\nKano,4000000\n")

    with open("cities.txt", "r") as f:
        lines = f.readlines()
        print("File content:")
        for line in lines:
            print(line.strip())

    total_population = 0
    for line in lines:
        parts = line.strip().split(",")
        total_population += int(parts[1])
    print("Total population from file:", total_population)

except FileNotFoundError:
    print("Error: File not found!")


# ==========================================================
# Problem 9: List Comprehensions
print("\n=== Problem 9 ===")

numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [n**2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
greater_than_5 = [n for n in numbers if n > 5]

print("Squares:", squares)
print("Even numbers:", evens)
print("Numbers >5:", greater_than_5)


# ==========================================================
# Problem 10: Error Handling
print("\n=== Problem 10 ===")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Invalid input! Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("Calculation completed")