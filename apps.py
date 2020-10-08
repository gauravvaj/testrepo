secret_word= "Gaurav"
guess=""
guess_count=0
guess_limit=3
outlimit= False
while guess!=secret_word and not(outlimit):
    if guess_count<guess_limit:
       guess= input("enter a guess: ")
       guess_count=guess_count+1
    else:
     doutlimit =True
if outlimit:
    print("out of guesses")
else:
    print("you win!")