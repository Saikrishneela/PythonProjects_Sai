import random

MAX_LINES=3
MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3

symbol_count={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def check_winning(columns,Lines,Bet,symbol_count):
    winnings=0
    winnings_lines=[]
    for line in range(Lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
             winnings+=symbol_count[symbol]*Bet  
             winnings_lines.append(line+1)
    return winnings,winnings_lines


def get_slot_machine_spin(rows,cols,symbol):
    all_symbols=[]
    for symbol,symbols_count in symbol_count.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
            
            
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
                
            else:
                print(column[row],end=" ")
        print()
def deposit():
    while True:
        amount=input("What would you like to deposit : ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("number must be greater than 0")
        else:print("Enter a Number")
    return amount

def get_number_of_lines():
    while True:
        Lines=input("Enter Number Of Lines To Bet on (1-"+str(MAX_LINES)+")? : ")
        if Lines.isdigit():
            Lines=int(Lines)
            if 1<=Lines<=MAX_LINES:
                break
            else:
                print("number must be greater than 0")
        else:print("Enter a Number")
    return Lines
    
def get_bet():
    while True:
        amount=input("What would you like to bet On Each Line: ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"number must be Between {MIN_BET} - {MAX_BET}.")
        else:print("Enter a Number")
    return amount

def spin(Balance):
    Lines=get_number_of_lines()
    while True:
        Bet=get_bet()
        Total_Bet=Bet*Lines
        if Total_Bet>Balance:
            print(f"You Do Not Have Enough To Bet That Amount,your current balance is {Balance}")
        else:
            break
    print(f"You Are Betting {Bet} on {Lines}. Total Bet is Equal To {Total_Bet}")
    print()
    
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winning(slots,Lines,Bet,symbol_count)
    print(f" Congratulations! You won {winnings}.")
    print(f"You won on Lines:",*winnings_lines)
    return winnings-Total_Bet

def main():
    Balance = deposit()
    while True:
        print(f"Current Balance is : {Balance}")
        start=input("Press Enter To Play (Q to quit).")
        if start==("Q" or "q"):
            break
        Balance+=spin(Balance)
    print(f"Balance in purse {Balance}.")
    
main()
        