# -----------------------------Task 1------------------------------------

# while True:
#     try:
#         name = input("Enter your name: ")
#         age = int(input("Enter your age: "))
#         if age < 0 or age > 130:
#             raise ValueError("Invalid age! Age has to be more than 0 and less tha 130.")
#         else:
#             print(f"Hi, {name}! Your age — {age}")
#             break
#     except ValueError as ve:
#         print("Error:", ve)

# -----------------------------Task 2------------------------------------


#           VARIANT 1


# def greet(name, age):
#     if age < 0 or age > 130:
#         raise ValueError("Invalid age! Age has to be more than 0 and less tha 130")
#     return f"Hi, {name}! Your age — {age}"

# while True:
#     try:
#         name = "x"
#         age = 14
#         message = greet(name, age)
#         print(message)
#         break
#     except ValueError as ve:
#         print("Error:", ve)


#           VARIANT 2


# def greet(name, age):
#     try:
#         if age < 0 or age > 130:
#             raise ValueError("Invalid age! Age has to be more than 0 and less tha 130")
#         return f"Hi, {name}! Your age — {age}"
#     except ValueError as ve:
#         return str(ve)

# name = "x"
# age = 14
# message = greet(name, age)
# print(message)


# -----------------------------Task 3------------------------------------

# try:
#     numbers = []

 
#     while True:
#         num_input = input("Enter positive number (or enter 'end', to end input and see results): ")
#         if num_input == 'end':
#             break
#         num = float(num_input)
#         if num > 0:
#             numbers.append(num)


#     if len(numbers) == 0:
#         raise ValueError("No positive numbers")

#     total = sum(numbers)
#     print("Sum of all positive numbers:", total)

# except ValueError as ve:
#     print("Error:", ve)

# -----------------------------Task 4------------------------------------


#           VARIANT 1


# def calculate_positive_sum(numbers):
#     total = sum(num for num in numbers if num > 0)
#     return total

# try:
#     numbers = [10, 5, -3]
#     if len(numbers) == 0:
#         raise ValueError("No positive numbers")

#     total = calculate_positive_sum(numbers)
#     print("Sum of all positive numbers:", total)

# except ValueError as ve:
#     print("Error:", ve)


#           VARIANT 2
    

# def calculate_positive_sum(numbers):
#     try:
#         total = sum(num for num in numbers if num > 0)
#         return total
#     except TypeError:
#         raise ValueError("List has invalid znachennya")

# try:
#     numbers = [10, 5, -3]
#     if len(numbers) == 0:
#         raise ValueError("No positive numbers")

#     total = calculate_positive_sum(numbers)
#     print("Sum of all positive numbers:", total)

# except ValueError as ve:
#     print("Error:", ve)

# ---------------------------------END------------------------------------