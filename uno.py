import random 
uno_cards = ["R0", "R1", "R1", "R2", "R2", "R3", "R3", "R4", "R4", "R5", "R5","R6","R6","R7", "R7","R8","R8","R9","R9","RS","RS", "RR","RR","R+2","R+2","WC", "Y0", "Y1", "Y1", "Y2", "Y2", "Y3", "Y3", "Y4", "Y4", "Y5", "Y5", "Y6", "Y6", "Y7", "Y7", "Y8", "Y8", "Y9", "Y9", "YS", "YS", "YR", "YR", "Y+2", "Y+2", "WC", "+4", "+4", "G0", "G1", "G1", "G2", "G2", "G3", "G3", "G4", "G4", "G5", "G5", "G6", "G6", "G7", "G7", "G8", "G8", "G9", "G9", "GS", "GS", "GR", "GR", "G+2", "G+2", "WC", "+4", "B0", "B1", "B1", "B2", "B2", "B3", "B3", "B4", "B4", "B5", "B5", "B6", "B6", "B7", "B7", "B8", "B8", "B9", "B9", "BS", "BS", "BR", "BR", "B+2", "B+2", "WC", "+4"]

print("Welcome to UNO! The game is pretty simple, you're dealt a hand of cards and you have to put down a card that matches either the letter or number of the top card. If you don't have a card in you hand that fits the criteriayou can put down a WC (Wild Card) which allows you to change the color to one of your choosing, a +4 card which allows you to change the color and forces the computer to draw four cards, or you can type \"draw\" which allows you to draw a card. Make sure that when you type what card you want to put down, that it is in all capital letters, for example \"B2\" instead of \"b2\". Let's Begin!!!!\n")

random.shuffle(uno_cards) 
deck = []
for num in range(7): 
    card = random.choice(uno_cards)
    deck.append(card)
    uno_cards.remove(card)

random.shuffle(uno_cards) 
a_deck = []
for num in range(7): 
    card = random.choice(uno_cards)
    a_deck.append(card)
    uno_cards.remove(card)

draw_pile = uno_cards
for cards in draw_pile:
    if card[0] == "R" or card[0] == "B" or card[0] == "Y" or card[0] == "G":
        first_card = card
        break
    else: 
        pass

def player(first_card, draw_pile, deck, a_deck):
    while len(deck) > 0:
        if len(a_deck) == 0:
            break
        else: 
            pass
        print("Your cards", deck)
        print("Top cards", first_card)
        next_turn = input("What card would you like to put down: ")
        next_card = next_turn
        if next_card in deck or next_turn == "draw":
            if next_card[0] == first_card[0] or next_card[1] == first_card[1]:
                deck.remove(next_card)
                first_card = next_card 
                draw_pile.append(first_card)
                if next_card[1] == "R" or next_card[1] == "S":
                    if len(deck) == 0: 
                        print("No cards left. You won!")
                        break
                    else:
                        player(first_card, draw_pile, deck, a_deck) 
                elif "+2" in next_turn and next_card[0] == first_card[0]:
                    a_deck.append(draw_pile[0])
                    a_deck.append(draw_pile[1])
                    draw_pile.append(next_card)
                    first_card = next_card
                    if len(deck) == 0: 
                        print("No cards left. You won!")
                        break
                    else: 
                        automated(first_card, draw_pile, a_deck, deck)
                else:
                    if len(deck) == 0: 
                        print("No cards left. You won!")
                        break
                    else:
                        automated(first_card, draw_pile, a_deck, deck)
            elif next_turn == "WC":
                deck.remove(next_card)
                color = input("Chose a color [R, B, Y, G]: ")
                first_card = str(color) + "-"
                if len(deck) == 0: 
                    print("No cards left. You won!")
                    break
                else:
                    automated(first_card, draw_pile, a_deck, deck)
            elif "+4" in next_card:
                deck.remove(next_card)
                for num in range(4):
                    a_deck.append(draw_pile[num])
                    del draw_pile[num]
                draw_pile.append(next_turn)
                color = input("Chose a color [R, B, Y, G]: ")
                first_card = str(color) + "-"     
                if len(deck) == 0: 
                    print("No cards left. You won!")
                    break
                else:
                    automated(first_card, draw_pile, a_deck, deck)
            elif next_turn == "draw":
                next_card = draw_pile[0]
                draw_pile.remove(next_card)
                print("You drew: ", next_card)
                if next_card[0] == first_card[0] or next_card[1] == first_card[1]:
                    print("You can play the card you drew")
                    draw_pile.append(next_card)
                    first_card = next_card
                    if next_card[1] == "R" or next_card[1] == "S":
                        player(first_card, draw_pile, deck, a_deck)
                    elif len(next_card) == 2: 
                        a_deck.append(draw_pile[0])
                        a_deck.append(draw_pile[1])
                        del draw_pile[0]
                        del draw_pile[1]
                        automated(first_card, draw_pile, a_deck, deck)
                    else:
                        automated(first_card, draw_pile, a_deck, deck)
                elif next_card == "WC": 
                    color = input("Pick a color [R, G, B, Y]: ")
                    first_card = color + "-"
                    draw_pile.append(next_card) 
                    automated(first_card, draw_pile, a_deck, deck)
                elif next_card == "+4":
                    for num in range(4):
                        a_deck.append(draw_pile[num])
                        del draw_pile[num]
                    color = input("Chose a color [R, B, Y, G]: ")
                    first_card = str(color) + "-"
                    draw_pile.append(next_card)
                    automated(first_card, draw_pile, a_deck, deck)
                else: 
                    print("You cannot play the card you drew")
                    deck.append(next_card)
                    automated(first_card, draw_pile, a_deck, deck)
            else: 
                pass
    
       
def automated(first_card, draw_pile, a_deck, deck):
    while len(a_deck) > 0:
        if len(deck) == 0:
            break
        for card in a_deck:
            if card[0] == first_card[0] or card[1] == first_card[1]:
                a_deck.remove(card)
                first_card = card 
                draw_pile.append(first_card)
                if card[1] == "R" or card[1] == "S":
                    print("The computer put down: ", card)  
                    if len(a_deck) == 0: 
                        print("No cards left. The computer won!")
                    else:
                        automated(first_card, draw_pile, a_deck, deck)
                    break
                elif "+2" in card:
                    print("The computer put down the card: ", card)
                    for num in range(2):
                        deck.append(draw_pile[num])
                        del draw_pile[num]
                    draw_pile.append(card)
                    first_card = card
                    if len(a_deck) == 0: 
                        print("No cards left. The computer won!")
                    else:
                        player(first_card, draw_pile, deck, a_deck)
                    break
                else:
                    print("The computer put down: ", card)
                    if len(a_deck) == 0: 
                        print("No cards left. The computer won!")
                    else:
                        player(first_card, draw_pile, deck,a_deck) 
                    break
            elif card == "WC":
                print("The computer put down: ", card)
                a_deck.remove(card)
                colors = ["R", "B", "Y", "G"]
                color = random.choice(colors)
                first_card = str(color) + "-"
                draw_pile.append(card)
                if len(a_deck) == 0: 
                    print("No cards left. The computer won!")
                else:
                    player(first_card, draw_pile,deck, a_deck)
                break
            elif card == "+4":
                print("The computer put down the card: ", card)
                a_deck.remove(card)
                for num in range(4):
                    deck.append(draw_pile[num])
                    del draw_pile[num]
                draw_pile.append(card)
                colors = ["R", "B", "Y", "G"]
                color = random.choice(colors)
                first_card = str(color) + "-"
                if len(a_deck) == 0: 
                    print("No cards left. The computer won!")
                else:
                    player(first_card, draw_pile, deck, a_deck)
                break
            elif card[0] != first_card[0] and card[1] != first_card[1]:
                pass
            else:
                pass
        if len(deck) > 0:
            print("The computer drawn a card")
            card = draw_pile[0]
            a_deck.append(card)
            draw_pile.remove(card)
            if card[0] == first_card[0] or card[1] == first_card[1]:
                print("The computer played the drawn card")
                if card[1] == "R" or card[1] == "S":
                    print("The computer put down: ", card)
                    first_card = card
                    automated(first_card, draw_pile, a_deck, deck)
                    break
                elif "+2" in card:
                    print("The computer put down: ", card)
                    first_card = card
                    for num in range(2):
                        deck.append(draw_pile[num])
                        del draw_pile[num]
                    player(first_card, draw_pile, deck, a_deck)
                    break
                else: 
                    print("The computer put down: ", card)
                    a_deck.remove(card)
                    draw_pile.append(card) 
                    first_card = card
                    player(first_card, draw_pile, deck, a_deck)
                    break
            elif card == "WC":
                print("The computer put down: ", card)
                a_deck.remove(card)
                colors = ["R", "B", "Y", "G"]
                color = random.choice(colors)
                first_card = str(color) + "-"
                draw_pile.append(card)
                player(first_card, draw_pile, deck, a_deck)
                break
            elif card == "+4":
                print("The computer put down the card: ", card)
                a_deck.remove(card)
                for num in range(4):
                    deck.append(draw_pile[num])
                    del draw_pile[num]
                draw_pile.append(card)
                colors = ["R", "B", "Y", "G"]
                color = random.choice(colors)
                first_card = str(color) + "-"
                player(first_card, draw_pile, deck, a_deck)
                break
            else:
                print("The drawn card was not played")
                player(first_card, draw_pile, deck, a_deck)
    
   
player(first_card, draw_pile, deck, a_deck)
