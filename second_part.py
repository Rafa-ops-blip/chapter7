# prompt = "\nTell me something, and i will repeat it back to you"
# prompt += "\nEnter 'quit' to end the program: "

# active = True
# while active:
#   message = input(prompt)

#   if message == 'quit':
#     active = False
#   else:
#     print(message)


#Pizza Toppings
def pizza_toppings():
  prompt = "\nEnter a pizza topping that you want or type 'quit' to quit: \n"
  toppings = ""
  while True:
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        print("Thanks for placing an order!")
        break
    else:
        print(f"Okay boss, I'll add {toppings} to your pizza order")
        

pizza_toppings()


#Movie tickets
def movie_ticket():
  while True:
    age_input = input("\nEnter your age, or type 'quit' to exit ")
    if age_input.lower() == 'quit':
        print("Thank you for using the movie ticket system. Goodbye!")
        break
    
    if age_input.isdigit():
        age = int(age_input)

        if age < 3:
            price = "free"
        elif 3 <= age <= 12:
            price = "$10"
        else:
            price = "$15"

        print(f"Your movie ticket is {price}.")
    else:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")


movie_ticket()


#Pizza Toppings with conditional statement
def pizza_toppings():
  prompt = "\nEnter a pizza topping that you want or type 'quit' to quit: \n"
  toppings = ""
  while toppings.lower() != 'quit':
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        print("Thanks for placing an order!")
        break
    else:
        print(f"Okay boss, I'll add {toppings} to your pizza order")
        

pizza_toppings()


#Pizza Toppings with conditional statement using active variable
def pizza_toppings():
  prompt = "\nEnter a pizza topping that you want or type 'quit' to quit: \n"
  active = True
  while active:
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        print("Thanks for placing an order!")
        break
    else:
        print(f"Okay boss, I'll add {toppings} to your pizza order")
        

pizza_toppings()


#Neverending loop number
def number():
    current_number = 1
    while current_number <= 14:
        print(current_number)
    

number()


#neverending loop 'string'
def string():
  prompt = "\nEnter a pizza topping that you want: \n"
  active = True
  while active:
    toppings = input(prompt)
    print(f"Okay sir, I'll add {toppings} to your pizza order")


string()




   



