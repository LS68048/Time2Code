# Checkout program

# -------------------------
# Subprograms
# -------------------------
def read_database():
    file = open("products.txt", "r")
    products = []
    for line in file:
        products.append(line.strip().split(","))
    return products


def get_product():
    number = input("Enter button number: ")
    if number == "":
        return -1
    elif not number.isdigit() or int(number) >= len(products):
        while not number.isdigit() or int(number) >= len(products):
            number = input("Enter button number: ")
    else:
        return int(number)


def output_product(button_number):
    print(products[button_number][1],"£" + products[button_number][2])


def transaction():
    product = 0
    price = 0
    while product != -1:
        product = get_product()
        output_product(product)
        price += float(products[product][2])
    print(f"Total: £{price:.2f}")

# -------------------------
# Main program
# -------------------------
products = read_database()
transaction()