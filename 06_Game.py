import random
print("\t\tWelcom to the game")
print("\t\tRock Paper Scissors")

user = 0
bot = 0

user_score = 0
bot_score = 0
while True:
    user_score = 0
    bot_score = 0
    for item in range(3):
        print("----------------Round # {}------------------".format(item+1))
        while True:
            user = input("\t[r] - rock;\n\t[p] - paper;\n\t[s] - scissors\n\tEnter your choice :")
            user = user.lower()
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print("Error")
                
        bot = random.choice('rps')
        print("\t User \t Bot ")
        print(f"\t  {user}\t  {bot}")
        if user=='r' and bot=='s' or user == 's' and bot == "p" or user=='p' and bot=='r':
            user_score+=1
        elif bot=='r'and user=='s' or bot == 's' and user=='p' or bot =='p' and user=='r':
            bot_score+=1
    if user_score > bot_score:
        print("============= Congratulation!!! User is winner !=====================")
    elif bot_score > user_score:
        print("============= Congratulation!!! Bot is winner !=====================")
    else:
        print("============= DRAW =====================")
    while True:
        user = input("Playe again ? [y] - YES, [n] - NO")
        user = user.lower()
        if user == 'y' or user == 'n':
            break
        else:
            print("Error. Enter your choice")
    if user == 'n':
        break
    
    
    
        
    