print("You're in a market because you need to buy fruits for your sick partner, an apple is 20 pesos and an orange is 25.")
apple_price = 20
orange_price = 25
apples_str = input("How many apples you want to buy? ")
oranges_str = input("How many oranges you want to buy? ")
apples = int(apples_str)
oranges = int(oranges_str)
print("The total amount is " + str(apples*apple_price + oranges*orange_price) + ".")