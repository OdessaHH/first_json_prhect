import json
import datetime

# Function to load clients from the json file
def load_clients():
    # open file (in read mode by default)
    with open("clients.json") as file:
        # load JSON data from the file
        data = json.load(file)
    return data["clients"]


# Function save clients to the json file
def save_clients(clients):
    # open the file in write mode
    with open("clients.json", "w") as file:
        # Dump (write) the clients to the json file
        json.dump({"clients": clients}, file)


def get_age(dob):
    # convert the dob from string to datetime object
    date_of_birth = datetime.datetime.strptime(dob, "%Y-%m-%d")
    # get current date
    today = datetime.datetime.today()
    # calculcation of age
    age = today.year - date_of_birth.year
    return age


def add_client(clients, name, dob, balance):
    # determining id of last client
    client_id = clients[-1]["client_id"] + 1
    # adding new client
    clients.append(
        {"client_id": client_id, "name": name, "dob": dob, "balance": balance}
    )
    # saving updated clients list to JSON file
    save_clients(clients)


def update_client(clients, client_id, name=None, dob=None, balance=None):
    # loop through client list
    for client in clients:
        # select client by id
        if client["client_id"] == client_id:
            # if name is provided, update clients name
            if name:
                client["name"] = name
            # if dob is provided, update clients dob
            if dob:
                client["dob"] = dob
            # if balance is provided, update clients balance
            if balance:
                client["balance"] = balance
            break
        elif client["client_id"] != client_id:
            print("Client does not exist.")
    # save updated clients list to JSON file
    save_clients(clients)


def delete_client(clients, client_id):
    # loop through client list
    for client in clients:
        # select client by id
        if client["client_id"] == client_id:
            # delete client
            del client
            # end loop to avoid unnecessary looping
            break
        elif client["client_id"] != client_id:
            print("Client does not exist.")
    # save updated client list to JSON
    save_clients(clients)


def display_client(clients, client_id):
    # looping through clients (list of dicts loaded from JSON file)
    for client in clients:
        # select client by id
        if client["client_id"] == client_id:
            # print client information
            print(f'Client ID {client["client_id"]}')
            print(f'Client Name {client["name"]}')
            print(f'Client DOB {client["dob"]}')
            print(f'Client Age {get_age(client["dob"])}')
            print(f'Client Balance {client["balance"]}')
        elif client["client_id"] != client_id:
            print("Client does not exist.")


# Function to display the total amount of money in the bank
def display_total(clients):
    # Calculate the total balance by adding up the balance of each client
    total = sum(client["balance"] for client in clients)
    # Print the total balance
    print("Total bank balance:", total)


# Function to transfer money from one client to another
def make_transfer(clients, sender_id, receiver_id, amount):
    sender = None
    receiver = None

    # Find the sender and receiver clients
    for client in clients:
        if client["client_id"] == sender_id:
            sender = client
        elif client["client_id"] == receiver_id:
            receiver = client
        elif client["client_id"] != sender_id or client["client_id"] != receiver_id:
            print("Client does not exist.")

    # Check if sender and receiver are found
    if sender is None:
        print("Sender not found.")
        return
    if receiver is None:
        print("Receiver not found.")
        return

    # Check if sender has sufficient balance for the transfer
    if sender["balance"] >= amount:
        # Update sender and receiver balances
        sender["balance"] -= amount
        receiver["balance"] += amount

        # Save the updated client data
        save_clients(clients)

        print("Transfer successful.")
        print("Sender balance:", sender["balance"])
        print("Receiver balance:", receiver["balance"])
        print("Amount transferred:", amount)
    else:
        print("Insufficient balance. Transfer failed.")


# Function to make VIP clients
def make_vip(clients, client_id):
    for client in clients:
        if client["client_id"] == client_id:
            if client["balance"] >= 10000:
                client["VIP"] = True
                print("Client is now a VIP.")
                print("Client balance:", client["balance"])
            else:
                client["VIP"] = False
                print("Client does not have enough balance to be a VIP.")
                print("Client balance:", client["balance"])
            break
    else:
        print("Client not found.")

    save_clients(clients)
