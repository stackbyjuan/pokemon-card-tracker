cards =[]
while True:   
    name = input("Enter the name of the card? ")
    value = int(input("Enter the value of the card? "))
    card = {
        "name": name,
        "value": value
    }
    cards.append(card)
    print(cards)
    print ("Do you want to add another card? (Yes/No)")
    answer = input()
    if answer.lower() == "no":
        break