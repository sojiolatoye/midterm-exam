from Product import Product



un = input("What is your username?")
ut = input("What is the type of product?")
unoi = int(input("Number of items?"))
if unoi < 0:
    print("number of items must be > 0")
uppi = float(input("What is the price per items all together?"))
if uppi < 0:
    print("Price must be > 0")
ud = input("Do you have a discount?")




p = Product(ut, unoi, uppi, ud )
p1  = (p.type, p.noi, p.ppi, p.discount)

print("HI",un)
print(p) 

