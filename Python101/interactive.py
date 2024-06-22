
name = input("What is your name?: ")
print(name)
print("Hello there",  name)
name_length = (len(name))
print ("Your name is ", name_length, "characters long!")

## injection by using F {}
print(f"Hello there {name}! Your name is {name_length} characters long!")
