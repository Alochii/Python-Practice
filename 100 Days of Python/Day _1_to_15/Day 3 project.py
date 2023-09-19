
print('''
*******************        TREASURE            HUNT         *******************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print(input("press enter to start the game"))
tryagain = "y"
while tryagain == "y":
    print('''
                        %%%%
                        %%%%-(
                    _%%%%%_/                        \ ' /
                    _%%%%%%%%                        - (_) -
                _%%%%%%%/ \%                        / , 
                %%%%%%%%%\\ \_
                %%%%%%   \ \\
                    )    /\_/
                    /(___. 
                    '----' (
                    /       )
        ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
                /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
                ,'          (         ```--.._= -_= -_= _-=- -_= _=-
            ,-'            )                 ``--._=-_ =-=_-= _-= _
            '-._    '-..___(                       ``-._=_-=_- =_-=
                ``---....__)                            `-._-=_-_=-
                    )|)|                                  `-._=-_
                    '-'-.\_                                    `-.
    ''')
    print("you wake up one day on the beach, you have no recollection of who you are or")
    print("where you are. the beach goes for as long as the eye can see, and infront of you")
    print("is a tall cliff. You can \n- type 'walk' to take a walk along the beach \n- type 'wait' to wait in place \n- type 'climb' to climb the cliff infront of you")
    choice = input()
    #wait is death
    #walk is cave
    #climb is fall and crack your skull
    if choice == 'wait':
        print("you wait for so long that you drift to sleep. never to wake up again.")
    elif choice == 'climb':
        print("you try to climb the cliff..but you're weak and feeble. you stumble back and break your neck.")
    elif choice == 'walk':
        print("you continue walking on the beach.")
        print("you find a break in the wall. it appears to be leading into the jungle. while on")
        print("the beach's horizon, you glimps what appears to be a structure of some kind. you can")
        print("- type 'walk' to continue walking towards the structure\n- type 'enter' to walk into the jungle")
        choice = input()
        #walk gets you to a weird temple
        #walk gets you into the jungle!
        if choice ==  'walk':
            print('''
                    <|
            A             
            /.\       
        <|  [""M#      
        A   | #              Avendar: The Crucible of Legends
        /.\ [""M#             [avendar.com 9999]
        [""M# | #  U"U#U                 
        | #  | #  \ .:/    
        | #  | #___| #     
        | "--'     .-"     
    |"-"-"-"-"-#-#-##    
    |     # ## ######     
        \       .::::'/     
        \      ::::'/      
    :8a|    # # ##      
    ::88a      ###       
    ::::888a  8a ##::.    
    ::::::888a88a[]::::
    :::::::::SUNDOGa8a::::. ..              
    :::::8::::888:Y8888:::::::::...      
    ::':::88::::888::Y88a______________________________________________________
    :: ::::88a::::88a:Y88a                                  __---__-- __
    ' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
    :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
    .::  :::::::::::::::::::Y88as88a...s88aa.
    ''')
            print("you see it in the distance, a towering palace! except.. its not. you've been walking")
            print("for so long and you get dehydrated and start hallucinating. you lie on the floor and die :DD")
        elif choice == 'enter':
            print('''
            |   [  | v':    :              |        |_,;c    
    | ]    |/; |,   |              |   [  ( __,/     
    |    ,-'/  ;\ ,<  _',\.-._,;   |      ] |    n   
    |   -' /   _;';    '=_'-' ,)  ,\        |   ,;   
    |  ]  / \,'__/--,_,-- 'mm'J -"_  ]       '-,+_   
    |    /    / "''-.,;"---''--'"" \      ]   __  "-'
    ;' [      / :    : _c           /         /  ",_,'
    |      [ | v|  , '/             c c    \ |        
    \    ]   |  \ /| :        __,-,v;|]   . \|        
    [      /"--'/  |      (7_   c@  )    )/|        
    \     ]    ,-"'<':       '--,    (    /^ |        
    | ]       / :   '|           \ |  )      |        
    | |   /  |  |    ;,-;,        \ ,)(     ]|        
    |  \^ |  |  :  |\ ,'           \ / \ [   |        
    |  ?  /  \_ |  /|:              | , \    |        
    |  | ('.   "--' |:,    ;        :\  ,\  [|        
    |  ;\~)   _     \_) ',_|   ,    | ),  \_ :        
    |   |/ [ /""-,_   '-'(    /.'   | \   |  '-_      
    | [      |  |  "---,__"'=';=,_  |  \ /|\    '"-,__
    |     ]  |  :    |    ""'^.\    |   | |    \      
    |  [    ]|  |    :              | ]  \ \   /  _AsH
    ''')
            print("you're in a jungle now unsurprisingly, you get bit by a snake. and you die.")
            print("its just a bad day. so every ending is the bad ending. Better luck next time")

    print('''
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄

    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    
    ''')

    tryagain= input("would you like to try again? Y/N\n").lower()