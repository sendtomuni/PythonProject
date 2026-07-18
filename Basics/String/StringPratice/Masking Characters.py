cardNumber = int(input("Enter a card number: "))

last4Digits = cardNumber % 10000

print("**** **** **** " + str(last4Digits))

cardNumber = input("Enter a card number: ")

last4DigitsStr = cardNumber[-4:]

dispNo = "**** **** **** " + str(last4DigitsStr)