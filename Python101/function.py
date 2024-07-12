
# def math(name):
#     print("Hello " + name)

# # math("Abdul")
# # math(name="Abdul")

# def math(a, b=5):
#     result = a + b
#     return result
# r = math(50)


# def arguments(x,y = 5): #parameters
# arguments(7)    #arguments

# def greet(name=None):
#     if name is None:
#         print("Hello, stranger!")
#     else:
#         print(f"Hello, {name}!")

# greet(None)        # Output: Hello, stranger!
# greet("None")  # Output: Hello, John!

# value = None
# if value is None:
#     print("No value assigned!")  # Output: No value assigned!

name = None

def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    global name
    name = first_name + " " + last_name

    return {"first": first_name, "last": last_name}

user = get_name()
# print("User first name is", user['first'])
# print("User Last name is", user['last'])
print(user['first'], user['last'])
print(name)

