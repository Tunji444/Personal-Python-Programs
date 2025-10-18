print("This can help you choose names")
answer=input("Do you wanna play a game with me  ")
if answer == ("Yes" or "yes"):
    print("Let's go")
elif answer != ("Yes" or "yes"):
    print("Cmon just one small game")   
    from time import sleep
    sleep(1)
    print("Let me show you ten names that start with a,b,c,d,e")
    sleep(1)
    letter=input("State the letter you want your name to begin with  ").lower()
    if letter == "a":
        print("Amelia, Ava, Aria, Abigail, Avery, Alexander, Asher, Aiden, Anthony, and Andrew.")
    elif letter == "b":
        print("Brooklyn, Brianna, Blake, Brittany, Bailey, Brooke, Beatrice, Bonnie.")
    elif letter == "c":
        print("Cabot, Cadby, Cade, Cadence, Cadew, Cadogan, Caedmon, Caelan, Chase, Cole")
    elif letter == "d":
        print("Daniel, David, Daisy, Damian, Dean ,Dante, Dominic, Daphne ,Deborah, Diana")
    elif letter == "e":
        print("Elizabeth, Eleanor, Emma, Easton, Evelyn, Ethan, Everett, Eliza, Elisha, Ezekiel.")
    elif letter != ("a") or ("b") or ("c") or ("d") or ("e"):
        print("Sorry I am not programmed to do that...")
