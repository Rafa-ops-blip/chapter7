# sandwiches
def list_of_sandwich():
    sandwich_orders = ['veges', 'ham', 'sardine', 'egg', 'butter']
    finished_sandwiches = []
    while sandwich_orders:
        sandwiches = sandwich_orders.pop()
        print(f"Ordered Sandwich: {sandwiches.title()}")
        finished_sandwiches.append(sandwiches)

        print(f"Heres your {sandwiches.title()} sandwich\n")


list_of_sandwich()


# sandwiches no 2
def list_of_sandwich():
    sandwich_orders = ['pastrami', 'ham', 'sardine', 'pastrami', 'egg', 'butter', 'pastrami']
    finished_sandwiches = []
    print("The deli has run out of pastrami")
    
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        # print(sandwich_orders)
    while sandwich_orders:
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
    print(finished_sandwiches)



list_of_sandwich()


#Dream Vacation
