import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)

def black_jack(check):
    if 11 in check and 10 in check:
        return True
    else:
        return False

def deal_for_pc(pc_cards):
    
    tot_sum = sum(pc_cards)

    while tot_sum <= 21:
        rand = random.choice(cards)
        if rand == 11 and tot_sum+11 > 21:
            rand = 1
        pc_cards.append(rand)
        tot_sum+=rand
    
    pc_cards.pop()
    
    return pc_cards

def print_values(my_cards,pc_cards,part):
    print(f"\tYour cards: {my_cards}, current score: {sum(my_cards)}")
    if part == 0:
        print(f"\tComputer's first card: {pc_cards[0]}")
    else:
        print(f"\tComputer cards: {pc_cards}, current score: {sum(pc_cards)}")

def start_game():
    print(logo)
    my_cards = [deal_card(),deal_card()]
    pc_cards = [deal_card(),deal_card()]
    
    print_values(my_cards,pc_cards,0)
    
    if black_jack(pc_cards):
        print_values(my_cards,pc_cards,1)
        print("You Lost, PC got Black Jack")
        return
    if black_jack(my_cards):
        print_values(my_cards,pc_cards,1)
        print("Yay! Your Lucky day, You got a Black Jack")
        return
    
    while input("Do you wish to Draw a card 'Y' or Stand back 'N': ").lower() == "y":
        rand = random.choice(cards)
        tot_sum = sum(my_cards)
        
        if rand == 11 and tot_sum+11 > 21:
            rand = 1
                
        my_cards.append(rand)
        
        if tot_sum+rand>21:
            print_values(my_cards,pc_cards,1)
            print("Shit! You went Over and lost")
            return
        
        print_values(my_cards,pc_cards,0)
    
    pc_cards = deal_for_pc(pc_cards)
    
    pc_sum = sum(pc_cards)
    my_sum = sum(my_cards)
    
    print_values(my_cards,pc_cards,1)
    
    if pc_sum == my_sum:
        print("It's a Draw!")
        return
    elif pc_sum < my_sum:
        print("Awsm! You Won")
        return
    else:
        print("Um! You Lost")
        return
    
    
    
    
if input("Do you wish to play a game of Black Jack? Yay or Nah!? ").lower() == "y":
    start_game()
  

