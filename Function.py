price = int(input("enterPriceHere :"))
def vat(price):
    total = price+(price*7/100)
    return total
print(vat(price))