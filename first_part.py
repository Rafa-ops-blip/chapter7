# prompt = "Please insert your name and "
# prompt += "Make sure its in capital letter: "

# name = input(prompt)
# print(f"\nHello {name}, welcome to this page")

#Type of rental car a user need
def car_rental():
  car = input("What type of rental car would you like? \n")
  print(f"Let me see if i can find you {car}\n")

car_rental()

#Restaurant Seating
def table_reservation():
  no_of_guests = int(input("How many guests are on your dinner table? "))
  if no_of_guests > 8:
    print("\nSorry, all the tables are occupied") 
    print("Wait for another table")
  else:
    print("Your table is ready")

table_reservation()

#Multiples of 10
def multiple_of_10():
  number = int(input("\nPick a number: "))
  if number % 10 == 0:
    print(f"The number {number} is a multiple of 10")
  else:
    print(f"The number {number} is not a multiple of 10")

multiple_of_10()