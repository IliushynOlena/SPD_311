
# test = "Hello"
# print(id(test))
# test += "!!!"
# print(id(test))
# print(len(test))

# line_1 = "Lorem ipsum dolor \"Python\" "
# line_2 = 'I love \n\t"Python"'
# line_3 = "\n - is the enter"
# line_3 = "\\n - is the enter"
# line_3 = r"\n - is the enter. \t - tabulation"
# img = '''
#                        ........     .....::....                       ..                            
#              :^  .......      ......           .........   ............  ..............             
#              .~                                                                       ^.            
#               ::                                                                      ^.            
#                ^.                                                                    ^.             
#                :.                                                                    ~              
#                7                                                                     ::             
#                !                  .^^^::::^^:.           ..::^^^^:.                   !             
#                .^              .~~:.        .:^~.     .~~:.     ..:^~^               ::             
#                 .:            7^                ^7. :7:              .~!            ^.              
#                 ^.           Y.          !777?~   ?J?    ^!~~:         .J.         !                
#                 ~           ^~         .#~7BP~?B  .B   7G!!?!7P.         Y         ^.               
#                :^           7:         :& ?@@~ &: :?   &J!@@B 5G         !:         !               
#                 ^.     :^^:^?J.         ^5???7Y^  ~7...^PYJJ~?G.         Y!..      ^.               
#                  .^   7.      7:           ..    ~    ^. .^^^.         !::...:~:  !                 
#                   ~   !   .57 .Y~.              !Y    ?.              :?  ..   ~^ ~                 
#                  ^.         ?~  .^~^:.     ..^~^.    ^^~^.         .:~~. .P~  .7. .^                
#                  7           ^7:    .:::::::.       .    .:^^^^^^^^:.  .7?    .    ~                
#                  ~             ^!^.                                 .^!~.         :.                
#                   ::             .^~~^..                       .:^~~:.           .^                 
#                     ~                ..:^~~!!^::.::::^^^^^7J~~^:.               .~                  
#                    ::                      Y~    ?!.:Y    .5                    :^                  
#                    ~.                      ^~^^::J   ?^^^^~!                    .~                  
#                     ^                                                           ~                   
#                     ~J.                                                       ^Y                    
#                     Y .^                                                     ^.?.                   
#                    .J .~                                                     :..J                   
#                    ^7 ::     ..::::.      ..:::..       ..                    ! Y                   
#                    :J  .??^^^:.....:^:^^J5~.. ..:YPJJ57::::^!J~^:^^^^^::^^^~^.  Y.                  
#                     :^Y^Y?                :^^:.^~B@@@#!~.:^^:.             ^G~J^:                   
#                       ?: P...       ...      .:: 7@@@? ::..                7~.Y                     
#                       .J 57:^YYYYYY?:^:?YYYYYYJ^Y@@@@@#!PGGGGG5~^~???????~^#.^7                     
#                        Y ^?  G#####Y   Y######P #@@@@@&.B#####G  :&&&&###. P J:                     
#                        :? G.                    .5@@@Y.                   ~7 5                      
#                         Y .Y..                    .^                  . ..P.:7                      
#                         ~^ .?YP^^^^^?5~~~~!!!Y?~~~~~~~~~~5Y~~^^^^~B7^^:?P!. ?:                      
#                         J.  5^P     .?^^^^^77J:          .^J?!Y!~^~    5^7  .J                      
#                        :? : ~JJ         ^G ~Y              Y .P        ?~5   !^                     
#                        .J 7^.#?7.        ?. J.            ~~ !^       .7P: Y..!                     
#                         7~ :G@@#J        :P^5J            BGYG       .5G@&J. J.                     
#                          :~^:?@B          &@@&           .@@@G        J@@~.^!.                      
#                             ..            G@@@^          ?@@@P         .^::                         
#                                           5^^77          5. .5                                      
#                                 .7YYJ7: ^GP  ^#         ~@~.^&#?:?G###P^                            
#                                ?@@@@@@@@@@@@&@@?        J@@@@@@@@@@@@@@@7                           
#                                P@@@@@@@@@@@@@@P          P@@@@@@@@@@@@@@~                           
#                                 ~G#&&&BGJ~JP?~.           .^!:.^7J5P5J~.                            
# '''
# print(line_1)
# print(line_2)
# print(line_3)
# print(img)

# myStr = "footbol"
# print(myStr[0])
# print(myStr[1])
# print(myStr[2])
# print(myStr[6])
# print(myStr[-1])
# print(myStr[-2])

# str1 = "Hello, "
# str2 = "admin."
# str4 = "You are cool"
# print(str1+ str2)
# str3 = str1 + str2 + str4
# print(str3)
# str5 = "Hello"
# print(str5*5)
# str6 = str5*5
# print(str6)
# print(len(str6))
# #name text... name text ..... age name text ...
# name = "Nazar"
# age= 15
# #formatLine = name + "text..." + name + "text..." + age + name + "text..."
# #formatLine = name + " text... " + name + " text... " + str(age) + " " + name + " text..."
# #formatLine = name , " text... " , name , " text... " ,age, name , " text..."
# #formatLine = " {}  text...  {}  text...  {} {} text...".format(name,name,age,name)
# #formatLine = " {0}  text...  {0}  text...  {1} {0} text...".format(name,age)
# formatLine = f" {name}  text...  {name}  text...  {age} {name} text..."
# print(formatLine)
# print(type(formatLine))
# salary = 15000.2
# print("Your salary is {0:15.3f}".format(salary))
# a = -15
# b = 33
# print(" A = {0:-} . B = {1:-}".format(a,b))
# print(" A = {0:+} . B = {1:+}".format(a,b))
# points = 12.2
# print(f"You have {points:<10.2f} points ")
# print(f"You have {points:>10.2f} points ")
# print(f"You have {points:^10.2f} points ")

for i in range(126):
    print(i, "--> ", chr(i), end="\t")
    # if i%7 == 0:
    #     print()
print(chr(65))
print(chr(90))
print(chr(9556), end="")
for i in range(20):
    print(chr(9552 ), end="")
print(chr(9559 ))


