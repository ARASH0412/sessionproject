# Variables
first_name = "johnny "
question = "How are you ?"
print("priya:", first_name, question)

# Strings
second_name = "Tony Sharma"
third_name = "What is this? 'Where is my money?' "
forth_name = "What\'s this? 'Where is my money?' "
print(second_name, third_name)
print(forth_name)

name = input("Please Enter your name: ")
print("Hi,{}. How are you dear?". format(name))

print(first_name + second_name)  # String Concatenation
print(first_name.title())  # String title method

# find method
my_book = "My favorite book is 'Elon Musk'.".find('book')
print(my_book)
c_name = "PARROT"
print(c_name.lower())
book = "My favorite book is 'Eloms Musk'.".replace('Eloms', 'Elon')
print(book)

address = "     23 DADAR    "
print(address.strip())
address1 = "101 main street \tdublin"
print(address1)
address2 = "102 main street \ndublin"
print(address2)

