"""Assignment: Develop a game of tic tac toe.
Author: A. Belén Chaparro"""

from colorama import Fore
from colorama.ansi import Style

def main():
    game = "on"
    while game == "on":
        # Get players' names with get_players_names function 
        # and store them in variables:
        player1, player2 = get_players_names()

        # Create and display tic tac toe grid:
        grid_numbers = create_grid()
        display_grid(grid_numbers)

        # Start game:
        make_move(player1, player2, grid_numbers)

        # End game:
        game = "off"

def get_players_names():
    """This function displays a title and greeting message, asks the players for
    their names and stores them in variables.
        Returns: Players' names.
    """

    print("\n----- TIC TAC TOE -----")
    print("We'll proceed to enter players' names: \n")

    player1 = input("Player 1, what is your name? ")
    print(f"Welcome {player1}! You'll be playing X's")

    player2 = input("\nPlayer 2, what is your name? ")
    print(f"Welcome {player2}! You'll be playing O's\n")

    return player1, player2

def create_grid():
    """This function creates a list with numbers from 1-9 that will be displayed
    in the tic tac toe grid.
        Returns: grid_numbers list. A list that contains numbers from 1-9."""

    grid_numbers = []
    for square in range(0,9):
        grid_numbers.append(square + 1)
    
    return grid_numbers

def display_grid(grid_elements):
    """This function displays the elements of the list passed as a parameter in a grid.
    The first element will be positioned in the upper left square. The following elements will be
    placed next to the previous one until a row of 3 elements is complete, then it will place the
    following elements in a new line, until all 9 elements are displayed.
        Parameters: A list of 9 elements.
        Returns: Nothing."""

    # First line:
    print(f"\n{Fore.CYAN} {grid_elements[0]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[1]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[2]}")
    print(f"{Fore.YELLOW} ─────────")
    # Second line:
    print(f"{Fore.CYAN} {grid_elements[3]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[4]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[5]}")
    print(f"{Fore.YELLOW} ─────────")
    #Third line:
    print(f"{Fore.CYAN} {grid_elements[6]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[7]} {Fore.YELLOW}│ {Fore.CYAN}{grid_elements[8]}{Style.RESET_ALL}\n")

def update_grid(grid_elements, position, player):
    """This function updates a list of 9 elements according to the information it receives
    as parameters. Then it calls the display_grid function to display the changes 
    made to the list.
        Parameters: 
            grid_elements: a list of 9 items.
            position: the number received from user input that determines the position where 
                they want to place their letter.
            player: a string that specifies the player that submitted a position.
        Returns: Nothing. """

    for i in range(0,9):
        if (position - 1) == i:
            if player == "player1":
                grid_elements[i] = "X"
                break
            else:
                grid_elements[i] = "O"
                break

    display_grid(grid_elements)

def make_move(player1, player2, grid_numbers):
    """This function allows the players to input the position of square where they want
    their mark to be in turns. It receives 3 parameters. Calls for the check_winner function
    to determine whether there is a winner or a draw, which makes the turns stop.
        Parameters:
            player1: The name of player 1.
            player2: The name of player 2.
            grid_numbers: a list of 9 items.
        Returns: Nothing. """

    moves =  True
    player = ""
    c = 1
    while moves == True:
        if c % 2 == 1:
            player = player1
            player_str = "player1"
        elif c % 2 == 0:
            player = player2
            player_str = "player2"
        
        player_move = int(input(f"{player.upper()}'s turn to choose a square(1-9): "))
        update_grid(grid_numbers, player_move, player_str)

        if c >= 4:
           moves = check_winner(player, player_str, grid_numbers)
        if c == 9:
            if moves == True:
                print(f"{Fore.BLUE}Draw! Good game. Thanks for playing!\n{Style.RESET_ALL}")
                break
        c+= 1

def check_winner(player, player_str, grid_elements):
    """This function checks every possible way of getting 3 marks in a row (horizontally, 
    vertically, or diagonally) to determine who is the winner. It receives 3 parameters.
    Prints a message with the winner.
        Returns: If a player got 3 marks in a row it returns False, to break the while loop
            that switches turns between players in the calling function make_move.
            If the previous statement is not achieved, it returns True, to remain in the
            turns loop until a winner is determined or the game ends in a draw."""
            
    if player_str == "player1":
        mark = "X"
    elif player_str == "player2":
        mark = "O"
    message_winner = f"{Fore.GREEN}Congratulations {player.upper()}, you win!\n{Style.RESET_ALL}"
    
    # First line:
    if grid_elements[0] == mark and grid_elements[1] == mark and  grid_elements[2] == mark:
        print(message_winner)
        return False
    # Second line:
    elif grid_elements[3] == mark and grid_elements[4] == mark and  grid_elements[5] == mark:
        print(message_winner)
        return False
    # Third line:
    elif grid_elements[6] == mark and grid_elements[7] == mark and  grid_elements[8] == mark:
        print(message_winner)
        return False
    # First column:
    elif grid_elements[0] == mark and grid_elements[3] == mark and  grid_elements[6] == mark:
        print(message_winner)
        return False
    # Second column:
    elif grid_elements[1] == mark and grid_elements[4] == mark and  grid_elements[7] == mark:
        print(message_winner)
        return False
    # Third column:
    elif grid_elements[2] == mark and grid_elements[5] == mark and  grid_elements[8] == mark:
        print(message_winner)
        return False
    # Decreasing diagonal:
    elif grid_elements[0] == mark and grid_elements[4] == mark and  grid_elements[8] == mark:
        print(message_winner)
        return False
    # Increasing diagonal:
    elif grid_elements[6] == mark and grid_elements[4] == mark and  grid_elements[2] == mark:
        print(message_winner)
        return False
    else:
        return True


# If this file is executed like this:
# > python tic_tac_toe.py then call the main function. 
# If this file is simply imported skip the call to main.
if __name__ == "__main__":
    main()
