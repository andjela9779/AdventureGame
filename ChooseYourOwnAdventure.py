def start_game():
    name = input("Enter your name: ")
    print("Welcome to the Adventure Game, " + name + "!")
    print("You are lost on a gravel road far away from the city and it has come to a dead end")
    print("You can either turn left or  right.Which way would you like to go?")
    print("1. Go left")
    print("2. Go right")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def go_left():
    print("You chose to go left.")
    print("You have come to a river.")
    print("You can either walk around it or swim across the river.")
    print("If you choose to walk around it, type walk.")
    print("If you choose to swim, type swim.")
    print("What would you like to do?")
    
    choice = input("Enter your choice: ")

    if choice == "walk":
        walk()
    elif choice == "swim":
        swim()
    else:
        print("Invalid choice. Please try again.")
        go_left()
    

def go_right():
    print("You chose to go right.")
    print("The sun has set and you have reached a forest.")
    print("You can choose to pick some berries in this forest for food, start a warm fire and go to sleep next to it or continue walking through the forest without food or sleep.")
    print("Please enter either food, fire or walk.You can only choose one.")
    
    choice = input("Enter your choice: ")

    if choice == "food":
        food()
    elif choice == "fire":
        fire()
    elif choice == "walk":
        keepWalking()
    else:
        print("Invalid choice. Please try again.")
        go_right()
    

def walk():
    print("You walked a few miles, ran out of water and lost the game.")
    

def swim():
    print("You swam across the river and found a bag of diamonds and a map that leads you back to the city. YOU WON THE GAME!!")

def food():
          print("You have been walking and haven't eaten in a few days now, but you have your berries with you.")
          print("However, you're not sure if the berries are poisonous or not.")
          print("You can choose to either take the risk and eat the berries or throw them away.")
          print("To eat the berries, type eat.")
          print("To throw away the berries, type throw.")
          choice = input("Type in your answer:")
          if choice == "eat":
            print("You're lucky!The berries were not poisonous.\n You refueled your energy and strength and managed to find your way back to the city.")
            print("YOU WON THE GAME!!")
          elif choice == "throw":
            print("You threw the berries away, but they were not actually poisonous...")
            print("Unlucky for you, you never found any other food along the way, and never found your way back to the city.")
            print("You lose the game.")
            
              

    
          
          

          

def fire():
    print("You weren't cautious enough due to being too exhausted and the fire you fell asleep next to,spread around while you were sleeping.")
    print("You lose the game.")


def keepWalking():
    print("You continued walking through the forest, found an old cabin,and a man living inside who gave you food and directions back to the city.")
    print("YOU WIN THE GAME!!")

start_game()

