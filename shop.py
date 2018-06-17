####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = ["The CupCake Town"]#complete me!
signature_flavors =["pistachio", "Oreo", "Red Velvet", "Trufle"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here! 
print("our menu is:")
for key, value in menu.items():

    print("- %s %s KD" ) % (key, value) 


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for eachItem in range(0,len(original_flavors)):
        print("- %s") % (original_flavors[eachItem])  # your code goes here!


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for sItem in range(0,len(signature_flavors)):
        print("- %s") % (signature_flavors[sItem]) # your code goes here!


def is_valid_order(order):
    
    if order == "vanilla" or order == "chocolate" or order == "strawberry" or order == "caramel" or order == "raspberry" or order == "pistachio" or order == "Oreo" or order == "Red Velvet" or order == "Trufle" or order == "coffee" or order == "tea" or order == "botteled water":
        return True
    else:
        return False

                

    

      
def get_order():
    order_list = []
    print("please type the exact spelling of your order, and to finish your order enter 'exit'")
    order = raw_input("type your order.")
    while order != "exit":
        if is_valid_order(order) == True:
            order_list.append(order)
        else:
            print("your order is not included in the menu")
        order = raw_input("enter more items.")
    return order_list

    


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total <= 5:
        return True
    elif total >= 5:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    for i in range(0,len(order_list)):
        for j in range(0,len(original_flavors)):
            if order_list[i] == original_flavors[j]:
                total = total + 2.000

        for j in range(0,len(signature_flavors)):
            if order_list[i] ==signature_flavors[j]:
                total = total + 2.750

        if order_list[i] == "coffee":
            total = total + 1.000

        elif order_list[i] == "tea":
            total = total + 0.900

        elif order_list[i] == "bottled water":
            total = total + 0.750
    if accept_credit_card(total) == True:
        print("your card is not eligible ")
    else:
        print("your card is eligible")

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for K in range(0,len(order_list)):
        print("- %s") % (order_list[K])
    print("your total payment is:%s KD ") % get_total_price(order_list)
    print("thank you for shoping in the %s ") % cupcake_shop_name
    # your code goes here!
