inputRound = int(input("EnterYourNum :"))
sum = 0
for x in range(inputRound):

    inputNumber = int(input("x"+str(x+1)+":")) 
    sum += inputNumber
print("Total :",sum)