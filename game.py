print('Welcome Tresure Island ')
print('Your mission is to find the tresure !')

print('''
 .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
Deelkar        #   `"._(_).       .(_)_."'   #
''')
direction = input('You/e in the middle of the way "left" or "right"').lower()

if direction == "left":
   left =  input('You have came to the lake , "swim" or "wait" \n').lower()
   if left == "wait":
       wait = input('You are in the final you have 3 rooms Choose : "yellow" "green"  "red" \n').lower()
       if wait == "yellow":
           print('You are Winner')
       elif wait == "red":
          print('You are buried , Game over')
       elif wait == "green":
        print('Game over , you choked on the green liquid ')
   else:
       print('Game over')
else:
    print('You fallaen in a hole , Game over !')