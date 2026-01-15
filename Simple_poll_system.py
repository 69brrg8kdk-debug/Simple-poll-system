poll = {"Yes": 0, "No": 0}

def vote():
    print("1. Yes")
    print("2. No")
    choice = input("Cast your vote: ")

    if choice == "1":
        poll["Yes"] += 1
    elif choice == "2":
        poll["No"] += 1
    else:
        print("Invalid vote")

def view_results():
    print("Poll Results:")
    for option, count in poll.items():
        print(option, ":", count)

def main():
    while True:
        print("1. Vote")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            vote()
        elif choice == "2":
            view_results()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
