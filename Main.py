# Lost & Found System 

lost_items = []

while True:
    print("\n===== Campus Lost & Found System =====")
    print("1. Add Lost/Found Item")
    print("2. View All Items")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        place = input("Enter place where lost/found: ")
        contact = input("Enter your contact: ")

        lost_items.append({
            "item": item,
            "place": place,
            "contact": contact
        })

        print("\nItem added successfully!")

    elif choice == "2":
        print("\n--- Lost & Found Items ---")
        if len(lost_items) == 0:
            print("No items added yet.")
        else:
            for i, it in enumerate(lost_items, start=1):
                print(f"{i}. {it['item']} - {it['place']} (Contact: {it['contact']})")

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
