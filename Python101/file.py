# file = open("dictionaries.py", "r")
# content = file.read()
# print(content)

file = open("dictionaries.py", "w")
file.write("Hello world")
file.close()

file = open("dictionaries.py", "r")
content = file.read()
print(content)