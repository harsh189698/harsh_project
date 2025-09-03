# project.py (log==with @.com)

users = {}   
cart = {}   


products = {
    1: ("Jeans", 100),
    2: ("Shirt", 200),
    3: ("T-shirt", 200),
    4: ("Jacket", 500)
}

def register():
    email = input("Enter your email: ")
    if "@" in email and ".com" in email:   
        password = input("Enter your password: ")
        users[email] = password
        print("Registration successful!\n")
    else:
        print("Invalid email... because @ and .com are complesarry")

def login():

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in users and users[email] == password:
        print("Login successful!\n")
        return True
    else:
        print("Login failed! Try again.\n")
        return False


def shopping():
    while True:
        print("\nProducts Available:")
        for pid, (pname, price) in products.items():
            print(f"{pid}. {pname} - Rs.{price}")

        choice = int(input("\nEnter product ID to add to cart (0 to exit): "))
        if choice == 0:
            break
        elif choice in products:
            qty = int(input("Enter quantity: "))
            if choice in cart:
                cart[choice] += qty
            else:
                cart[choice] = qty
            print("Added to cart!")
        else:
            print("Invalid product ID!")

    print("\nYour Final Cart:")
    total = 0
    for pid, qty in cart.items():
        pname, price = products[pid]
        print(f"{pname} x {qty} = Rs.{price * qty}")
        total += price * qty
    print(f"Total Amount: Rs.{total}")


while True:
    print("\n1. Register\n2. Login\n3. Exit")
    option = input("Choose option: ")

    if option == "1":
        register()
    elif option == "2":
        if login():
            shopping()
    elif option == "3":
        print("Goodbye!")
        break
        
        
    else:
        print("Invalid choice!")