from time import sleep
shows = input("What is your favourite show: ")
with open('shows.txt', 'a') as file:
  file.write(shows)
  print("Your favourite show has been saved")
print("...")
sleep(2)
print("looking up your favourite shows ...")
sleep(1)
with open('shows.txt', 'r') as file:
   fav_shows = file.read()
   sleep(2)
   print(f"Your favourite show is {fav_shows}.")