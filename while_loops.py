# def print_name():
#   name = input("What is your name?\n")
#   age = int(input("What is your age: "))
#   age += 5
#   level = input("Your current level is: ")
#   print(f"Hello {name}, you are {age} years old and you're in {level} level.")

# print_name()

# def input_division():
#   number = int(input("Write any number: "))
#   if number % 3:
#     print(f"The number {number} is a multiple of 3")
#   else:
#     print(f"The number {number} is not divisible by 3")

# input_division()

#while loop
# 23

# def user_prompt():
#   prompt = "Tell me anything and i'll print it back\n"
#   message = ""
#   while message != "quit":
#     message = input("prompt: ")
#     print(prompt, message)
#   print("You've finally quit the program")

# user_prompt()

def continue_demo():
  number = 0
  while number < 8:
    number += 1
    if number % 2 == 0:
      continue
    print(number)

continue_demo()
