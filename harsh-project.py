#project.py

users = {}  
cart = {}   

products = {
    1: ("Jeans", 100),
    2: ("Shirt", 200),
    3: ("T-shirt", 200),
    4: ("Jacket", 500)
}

def show_products():
    print("\n--- Products ---")
    for pid, (name, price) in products.items():
        print(f"{pid}. {name} - ₹{price}")
    print("5. Checkout")
    print("0. Exit")
    
    while True:
        print("\n1. Login")
        print("2. Register")
        print("0. Exit")
        choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("Login successful...")
            
           


            while True:
                show_products()
                opt = input("Choose product: ")

                if opt == "0":
                    print("Exiting... ")
                    exit()

                elif opt == "5":
                    total = sum(products[pid][1] * qty for pid, qty in cart.items())
                    print("\n--- Checkout ---")
                    for pid, qty in cart.items():
                        name, price = products[pid]
                        print(f"{name} x {qty} = ₹{price * qty}")
                    print(f"Total = ₹{total}")
                    cart.clear()
                    break  

                elif opt.isdigit() and int(opt) in products:
                    qty = int(input("Enter quantity: "))
                    pid = int(opt)
                    cart[pid] = cart.get(pid, 0) + qty
                    print(f"Added {qty} x {products[pid][0]} to cart")
                else:
                    print("Invalid choice!")

        else:
            print("Invalid login...")

    elif choice == "2":
        username = input("Choose username: ")
        password = input("Choose password: ")
        users[username] = password
        print("Registered successfully...")

    elif choice == "0":
        print("Goodbye ...")
        break

    else:
        print("Invalid option, try again.")