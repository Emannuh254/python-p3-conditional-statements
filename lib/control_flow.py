# username = input("Please input username: ")
# password = input("Please input password: ")

# # Admin login function
# def admin_login(username, password):
#     # Check if the username and password match
#     if (username == "admin" or username == "Admin") and password == "12345":
#         print("Access granted.")
#     else:
#         print("Access denied.")


# admin_login(username, password)
def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


print(admin_login("sudo", "12345"))  # access denied
print(admin_login("admin", "12345"))  # access granted
print(admin_login("ADMIN", "12345"))  # access granted
print(admin_login("user", "wrong"))   # access denied

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 60:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(40))


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print(fizzbuzz(1))  # 1
print(fizzbuzz(2))  # 2
print(fizzbuzz(3))  # Fizz
print(fizzbuzz(4))  # 4
print(fizzbuzz(5))  # Buzz
print(fizzbuzz(15)) # FizzBuzz


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:       # check division by zero
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        print("Invalid operation!")
        return None


print(calculator("+", 1, 1))  # 2
print(calculator("-", 3, 1))  # 2
print(calculator("*", 3, 2))  # 6
print(calculator("/", 4, 2))  # 2
print(calculator("nope", 4, 2))  # invalid operation!" -> None

