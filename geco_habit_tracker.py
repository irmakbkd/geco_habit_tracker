""" Note: If you run this app for the first time and your system blocks standard input,
the app will assign a default username ('Guest') to prevent crashing. """


# imports
import sys
import time
import json
import os


# slow print function
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# fast print function
def fast_print(text, delay=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# get username
def get_user_name():
    try:
        with open("user_name.txt", "r") as file:
            user_name = file.read().strip()
            if user_name:
                return user_name
    except FileNotFoundError:
        pass

    slow_print("\nWelcome to 'Geco Habit Tracker'! \n" \
               "This app is designed to help you track your daily habits. \n" \
                "Try not to break the chain as you build your routines! \n")
    
    try:
        user_name = input("Please enter your name: ").strip()
    except EOFError:
        slow_print("\nAn unexpected input error occurred. Please restart the app. >.<\n")
        return "Guest"
    
    if user_name:
        with open("user_name.txt", "w") as file:
            file.write(user_name)
        return user_name
    else:
        slow_print("No name entered. Using 'Guest' as default. \n")
        return "Guest"


# menu
def menu():
    fast_print("="*34)
    fast_print("|    1- Add a new habit          |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    2- Delete a habit           |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    3- Mark habit status        |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    4- See all habits           |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    5- Completed habits         |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    6- Uncompleted habits       |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    7- Change username          |")
    fast_print("|" + "_"*32 + "|")
    fast_print("|    8- Exit                     |")
    fast_print("="*34)
    fast_print("\n")


# choose an option from menu
def main():
    user_name = get_user_name()
    slow_print(f"\nHello {user_name}, Welcome to 'Geco Habit Tracker'! ^.^ \n" \
        "This app is designed to help you track your daily habits. \n" \
        "Try not to break the chain! \n")    

    while True:
        menu()
        choice = input("Please choose an option from the menu: ").strip()

        if choice == "1":
            add_habit()
        
        elif choice == "2":
            delete_habit()

        elif choice == "3":
            mark_habit_status()

        elif choice == "4":
            see_all_habits()

        elif choice == "5":
            completed_habits()

        elif choice == "6":
            uncompleted_habits()

        elif choice == "7":
            change_user_name()

        elif choice == "8":
            slow_print(f"\nGoodbye {user_name}! ^.^ \n")
            input("To exit press Enter...")
            break

        else:
            slow_print("\nInvalid choice. Please try again! >.<\n")


# load habits
def load_habits():
    if not os.path.exists("habits.json"):
        with open ("habits.json", "w") as file:
            json.dump({}, file)
    with open ("habits.json", "r") as file:
        return json.load(file)


# save habits
def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent = 4)


# add a new habit
def add_habit():
    habits = load_habits()

    while True:
        name = input("\nEnter the name of the habit you want to add (type m to return to menu): ").strip()
        if name.lower() == "m":
            slow_print("Returning to menu... \n")
            return
        
        if name in habits:
            slow_print("\nThis habit already exists. Please enter a different name. ")
        
        elif name.strip() == "":
            slow_print("\nHabit name cannot be empty. ")
        else:
            break

    while True:
        try:
            goal_days = int(input("\nHow many days do you want this habit to continue? (Max 100): "))
            if 1 <= goal_days <= 100:
                break
            else:
                slow_print("\nPlease enter a number between 1 and 100.")

        except ValueError:
            slow_print("\nPlease enter a valid number. >.<")

    habits[name] = [None] * goal_days

    save_habits(habits)
    slow_print(f"\n'{name}' habit has been added successfully! ^.^ \n")


# delete a habit
def delete_habit():
    habits = load_habits()

    if not habits:
        slow_print("\nThere are no habits to delete. \n")
        return
    
    habit_list = list(habits.keys())
    slow_print("\n~~ Your Current Habits ~~ \n")
    for i, habit in enumerate(habit_list, start = 1):
        slow_print(f"{i}. {habit}")

    while True:
        user_input = input("\nEnter the number of the habit you want to delete (type m to return to menu): ").strip()

        if user_input.lower() == "m":
            slow_print("Returning to menu... \n")
            return

        try:
            choice = int(user_input)
            if 1<= choice <= len(habit_list):
                habit_name = habit_list[choice -1]
                del habits[habit_name]
                save_habits(habits)
                slow_print(f"\n'{habit_name}' has been deleted. \n")
                break
            else:
                slow_print(f"\nPlease enter a number between 1 and {len(habit_list)}. \n")
        except ValueError:
            slow_print(f"\nPlease enter a valid number. >.< \n")


# mark habit status as done or undone
def mark_habit_status():
    habits = load_habits()

    if not habits:
        slow_print("\nNo habits to mark. \n")
        return
    
    habit_list = [h for h in habits if None in habits[h]]

    if not habit_list:
        slow_print("\nAll habits are fully marked! ^.^\n")
        return

    slow_print("\nWhich habit do you want to mark for today? \n")
    for i, habit in enumerate(habit_list, start = 1):
        slow_print(f"{i}. {habit}")
    
    while True:
        choice = input("\nEnter the number (type m to return to menu): ")

        if choice.lower() == "m":
            slow_print("Returning to menu... \n")
            return

        try:
            index = int(choice)
            if 1 <= index <= len(habit_list):
                habit_name = habit_list[index - 1]
                progress = habits[habit_name]

                for i in range(len(progress)):
                    if progress[i] is None:
                        while True:
                            slow_print("\n1. Mark as done [+]")
                            slow_print("2. Mark as missed [-]")
                            slow_print("3. Cancel")
                            
                            status = input("\nPlease choose an option: ").strip()
                            if status == "1":
                                progress[i] = "done"
                                save_habits(habits)
                                slow_print(f"\nMarked day {i+1} as [+] for '{habit_name}'! ^.^\n")
                                break
                            elif status == "2":
                                progress[i] = "missed"
                                save_habits(habits)
                                slow_print(f"\nMarked day {i+1} as [-] for '{habit_name}'! >.<\n")
                                return
                            elif status == "3":
                                slow_print("Canceled. \n")
                                return
                            else:
                                slow_print("Invalid choice, please choose 1,2 or 3.")

                        return

        except ValueError:
            slow_print("Please enter a valid number.")


# see all habits
def see_all_habits():
    habits = load_habits()

    if not habits:
        slow_print("\nNo habits added yet. \n")
        return
    
    slow_print("\n~~ Your Current Habits ~~ \n")

    labels = []
    habit_progress_pairs =[]
    for i, (habit, progress) in enumerate(habits.items(), start = 1):
        if all(progress) or "missed" in progress:
            continue

        done = progress.count("done")
        total = len(progress)
        label = f"{i}. {habit} ({done}/{total})"
        labels.append(label)
        habit_progress_pairs.append((label, progress))

    if not labels:
        slow_print("\nAll habits are completed! ^.^\n")
        return
    
    max_len = max(len(label) for label in labels)

    for label, progress in habit_progress_pairs:
        slow_print(label.ljust(max_len))
        indent = ' ' * max_len
        total = len(progress)
        for j in range(0, total, 20):
            line = progress[j:j+20]
            bar = ''.join('[+]' if day == "done" else '[–]' if day == "missed" else '[ ]' for day in line)
            fast_print(indent + bar)
        fast_print("\n")


# completed habits
def completed_habits():
    habits = load_habits()
    completed = []

    for habit, progress in habits.items():
        if all(day == "done" for day in progress):
            completed.append((habit, len(progress)))
    
    if completed:
        slow_print("\n~~ Completed Habits ~~ \n")
        for i, (habit, total) in enumerate(completed, start = 1):
            slow_print(f"{i}. {habit} ({total} days)")
        slow_print("\n")
    else:
        slow_print("\nNo habits have been fully completed yet. >.<\n")


# uncompleted habits
def uncompleted_habits():
    habits = load_habits()
    uncompleted = []

    for habit, progress in habits.items():
        if "missed" in progress:
            broken_day = progress.index("missed") + 1 
            uncompleted.append((habit, broken_day))

    if uncompleted:
        slow_print("\n~~ Uncompleted Habits (Broken Chains) ~~ \n")
        for i, (habit, day) in enumerate(uncompleted, start = 1):
            slow_print(f"{i}. {habit} (Broken on day {day})")

        slow_print("\n")
    else:
        slow_print("\nNo habits have been broken so far, keep going! ^.^\n")


# change username
def change_user_name():
    try:
        new_name = input("\nPlease enter your new username (type m to return to menu): ").strip()
        if new_name.lower() == "m":
            slow_print("Returning to menu... \n")
            return
        if not new_name:
            slow_print("\nUsername cannot be empty. \n")
            return
        with open("user_name.txt", "w") as file:
            file.write(new_name)
        slow_print(f"\nUsername successfully changed to '{new_name}'! ^.^\n")
    
    except Exception as e:
        slow_print("\nAn error occurred while changing the username. >.<")
        print(e)


if __name__ == "__main__":
    main()







