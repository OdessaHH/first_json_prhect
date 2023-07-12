import demo as banking


def main():
    while True:
        print("\n1. Add new client")
        print("2. Update existing client")
        print("3. Delete client")
        print("4. Display client")
        print("5. Display total")
        print("6. Make transfer")
        print("7. Make VIP")
        print("8. Exit")

        option = int(input("\nSelect an option: "))

        if option == 1:
            name = input("Enter new client name: ")
            dob = input("Enter new client DOB (YYYY-MM-DD): ")
            balance = float(input("Enter client balance: "))
            banking.add_client(banking.load_clients(), name, dob, balance)
            print("Client added successfully.")
        elif option == 2:
            client_id = int(input("Enter client ID: "))
            name = input("Enter new client name (leave empty to keep current): ")
            dob = input(
                "Enter new client DOB (YYYY-MM-DD) (leave empty to keep current): "
            )
            balance = input("Enter new client balance (leave empty to keep current): ")
            banking.update_client(banking.load_clients(), client_id, name, dob, balance)
            print("Client updated successfully.")
        elif option == 3:
            id = int(input("Enter client ID: "))
            banking.delete_client(banking.load_clients(), id)
            print("Client deleted successfully.")
        elif option == 4:
            id = int(input("Enter client ID: "))
            banking.display_client(banking.load_clients(), id)
        elif option == 5:
            banking.display_total(banking.load_clients())
        elif option == 6:
            sender = int(input("Enter sender ID: "))
            receiver = int(input("Enter receiver ID: "))
            amount = float(input("Enter amount: "))
            clients = banking.load_clients()
            banking.make_transfer(clients, sender, receiver, amount)
        elif option == 7:
            clients = banking.load_clients()
            client_id = int(input("Enter client ID: "))
            banking.make_vip(clients, client_id)
        elif option == 8:
            break
        else:
            print("Invalid option. Please try again.")


main()
