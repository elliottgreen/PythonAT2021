secret_number = 777

print(
        ''' 
         +================================+
         | Welcome to my game, muggle!    |
         | Enter an integer number        |
         | and guess what number I've     |
         | picked for you.                |
         | So, what is the secret number? |
         +================================+
        ''') 

number = 9999
# 0 terminates execution.
while number != 0:
    number = int(input("Guess my number or type 0 to give up: "))
    if number == secret_number:
       #number = secret_number
       print ("Well done, muggle! You are free now.")
       break
    else:
        print ("Ha ha! You're stuck in my loop!")

# number = int(input("Guess my number or type 0 to give up: "))
