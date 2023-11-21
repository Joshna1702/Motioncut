import time

def introduction():
    print("Welcome to the Time-Traveling Odyssey!")
    time.sleep(1)
    print("You stumble upon a peculiar artifact in an old bookstore - a mysterious pocket watch.")
    time.sleep(1)
    print("As you touch the watch, a blinding light surrounds you, and you find yourself in a different era.")
    time.sleep(1)
    print("The pocket watch starts ticking, and you realize it's your key to navigating through time.")

def choose_era():
    print("You find yourself in a bustling marketplace.")
    time.sleep(1)
    print("You notice people dressed in medieval attire, horses, and market stalls selling exotic goods.")
    time.sleep(1)
    return input("Do you want to 1.'Explore the Medieval Market' or 2.'Activate the Watch' to travel to a different era? Choose either 1 0r 2:")

def medieval_market():
    print("You decide to explore the medieval market.")
    time.sleep(1)
    print("As you wander through the market, you encounter a mysterious fortune teller.")
    time.sleep(1)
    print("She offers to reveal your future. Do you accept?")

    fortune_choice = input("Type 'yes' or 'no': ").lower()

    if fortune_choice == "yes":
        print("The fortune teller gazes into her crystal ball and reveals visions of your future.")
        time.sleep(1)
        print("The visions include challenges and triumphs you may face in your journey through time.")
    else:
        print("You politely decline the offer and continue exploring the market.")

def activate_watch():
    print("You choose to activate the pocket watch and travel to a different era.")
    time.sleep(1)
    print("The watch emits a soft hum, and you find yourself in a futuristic city.")
    time.sleep(1)
    print("Skyscrapers tower above, and hovercrafts zip through the air.")
    time.sleep(1)
    print("You can't help but marvel at the advanced technology.")

def futuristic_city():
    print("You explore the futuristic city and encounter a group of scientists working on groundbreaking inventions.")
    time.sleep(1)
    print("They offer to upgrade your pocket watch with advanced time-traveling capabilities.")
    time.sleep(1)
    return input("Do you accept the upgrade? Type 'yes' or 'no': ").lower()

def accept_upgrade():
    print("You accept the upgrade, and the scientists enhance your pocket watch.")
    time.sleep(1)
    print("Now, you can choose specific years and destinations for your time-traveling adventures.")
    time.sleep(1)
    print("Your journey through time becomes more controlled and intentional.")

def decline_upgrade():
    print("You decline the upgrade and decide to continue your time-traveling journey with the original capabilities of the pocket watch.")
    time.sleep(1)
    print("You bid farewell to the scientists and explore more eras.")

def unexpected_twist():
    print("As you continue your time-traveling odyssey, you encounter an unexpected twist.")
    time.sleep(1)
    print("A mysterious figure appears and warns you about the consequences of altering the course of history.")
    time.sleep(1)
    print("You must now make a choice - 'Return to Your Original Time' or 'Continue Exploring, Consequences Be Damned'.")

def return_to_original_time():
    print("You decide to heed the warning and return to your original time.")
    time.sleep(1)
    print("As you activate the pocket watch, you find yourself back in the old bookstore.")
    time.sleep(1)
    print("The adventure may be over, but the memories of your time-traveling odyssey will stay with you forever.")

def consequences_be_damned():
    print("You choose to continue exploring, consequences be damned.")
    time.sleep(1)
    print("As you travel through different eras, you witness both the wonders and tragedies of history.")
    time.sleep(1)
    print("Your actions have lasting effects on the timeline, shaping the course of events.")

# Main game flow
introduction()

era_choice = choose_era()

if era_choice == "1":
    medieval_market()

elif era_choice =="2":
    activate_watch()

futuristic_city_choice = futuristic_city()

if futuristic_city_choice == "yes":
    accept_upgrade()
else:
    decline_upgrade()

unexpected_twist()

final_choice = input("Choose option 1.'return to your original time' or 2.'continue exploring, consequences be damned'. Type 1 or 2: ")

if final_choice == "1":
    return_to_original_time()
elif final_choice == "2":
    consequences_be_damned()
else:
    print("Invalid choice. The time-traveling odyssey ends.")
