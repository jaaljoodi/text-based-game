# Jaber Aljoodi 

#the program
def showInstructions():
    #Print a main menu and the commands
    print("-------------------------------------")
    print("   --- Dragon Text Adventure Game ---")
    print('-------------------------------------')
    print("-instructions:")
    print("    -Move commands: < South, North, East, West > ")
    print("    -Add to Inventory: 'item name'")
    print("    -Collect 6 items to win the game or be eaten by the dragon")
    print('------------------------------------------')


def showStatus(currentRoom,inventory,rooms):
    #print the player's current status, inventory
    #print an item if there is one on the list.
    print(f'You are in the {currentRoom}')
    print(f'Inventory: {inventory}')
    print('Rooms Available:')
    print('---------------------------------')
    #Loop through all the available rooms in the dictionary
    #Display the rooms after moving
    for i,j in rooms.items():
        print(i)
    print('---------------------------------')

def validateDirections(direction):
    #A list of valid directions
    validDirections=['North','South','West','East']
    #If the direction is valid then the function will allow the player to progress
    #Otherwise the function will prompt the user that the command is invalid
    #It will request they provide the correct command direction.
    if direction in validDirections:
        return True
    return False


def main():
    #define an inventory,which initially empty
    inventory=[]
    #a dictionary linking a room to other rooms
    rooms={
            #Room     Direction   Room
            'Blanquilla':{'East':'Curato','South':'Block','item':'Yourgut'},
            'Curato':{'West':'Blanquilla','item':'Cutlass'},
            'Block':{'North':'Blanquilla','West':'Grenada','South':'Antania','item':'Treasure Ship'},
            'Grenada':{'East':'Block','item':'Cannons'},
            'Botafo':{'West':'Block','North':'Maui','item':'Frigate'},
            'Maui':{'South':'Botafo','item':'Villan'},
            'Antania':{'North':'Block','East':'Nantucket','item':'Rum'},
            'Nantucket':{'West':'Antania','item':'Gold'}
        }
    #Start the player in the Hall.
    currentRoom='Blanquilla'
    #Declare the direction variable 
    # that will acting as the place holder for the direction entered by the player
    direction=''
    won=False
    #Show the player the game instructions
    showInstructions()

    #ultimate loop breaker
    breaker=True
    #loop forever
    while breaker:
        if len(inventory)!=6:
            #show player's status
            # showStatus(currentRoom,inventory,rooms)
            #Request the player to enter a direction to move to the next room
            direction=input('Enter your move < South,North,East,West >')
            #using the function we defined check wheather the move is valid or not
            #If the move is valid, continue in the game otherwise if direction is exit leave the game or else
            #request the player to enter the direction again.
            if validateDirections(direction):
                #continue with the game
                item='item' #This is the keyword that will be used to fetch the item in a dictionary for each room.
                for i,j in rooms.items(): #Iterate through the rooms and respective moves to other rooms
                    # print('This is the room we are in: '+str(i))
                    
                    if direction in j: #check wheather the direction entred is contained in nested dictionary
                        #Change the current room to the room the player moves to.
                        currentRoom=j.get(direction)
                        collectables=j.get(item) #Get the name of the item in that particular room.
                        rooms.pop(i)
                        #If the collectable is a villan, then end the game at that point otherwise collect the item
                        if collectables!='Villan':
                            print(f'Found a {collectables} collect it by typing its name')
                            take=input('>')
                            if take==collectables: #Ensure what is typed is the same name as the item in the room otherwise won't collect
                                print('--------------------------')
                                print(f'    {take} retrieved!')
                                #After successfully collecting the item add it to the inventory list
                                inventory.append(take)
                            else:
                                #Otherwise if your type the wrong name, oops you lose the item!
                                print('oops, maybe a wrong spelling!')
                                break
                        else:
                            #if you encounter a villan hidding as a collectable item, you lose!
                            print('--------------------------')
                            print('OOH OOH Entered a Villan zone... Game Over')
                            breaker=False
                        
                        # rooms.pop(currentRoom)
                        
                        # print(collect)
                        #show the status that the player is in i.e current room, a list of inventories and 
                        # the rooms that are yet to be explored:
                        showStatus(currentRoom,inventory,rooms)
                        print('-------------------------------------')
                        break
                    else:
                        print('Cannot move in that direction')
                        break
                
                #conditional to exit while loop if item in room is dragon
                    #Print losing message
            
                
            elif direction=='exit':
                #When the user types exit, the game will end there and print the progress so far.
                print('Sorry to see you leave..see you next time')
                print('Current room: '+str(currentRoom))
                print('You managed to collect: '+str(inventory))
                breaker=False
            #Incase the player enters a command not allowed, request they provide the correct moves again
            else:
                print('Invalid move command...try again! Valid commands: < South, North, East, West >')
                print('---------------------------------')

        else:
            #if the inventory has 6 items collected, exit the game and show the user that they have won
            print('----------------------------------------------------------------------')
            print('           *****Congratulations:Dragon Master******                    ')
            print('                  You won by Collecting 6 items')
            print(f'                items collected: {inventory}           ')
            print('-----------------------------------------------------------------------')
            breaker=False


if __name__=="__main__":
    main()
