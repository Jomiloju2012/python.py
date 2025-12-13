import json
from datetime import date

file="sales.json"

def add_sales():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity sold: "))
    sale_date = date.today()
    amount = float(input("Enter sale amount: "))
    totalamount = quantity * amount

    sale_record = {
        "item": item,       
        "quantity": quantity,
        "date": sale_date.isoformat(),
        "amount": amount,
        "totalamount": totalamount
    }

    print("sale_record", sale_record)

    try:
        with open(file, "r") as f:
            sales_data = json.load(f)   
    except FileNotFoundError:
        data=[sale_record]
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    print("Sales data saved successfully.")


def view_sales():

    try:
        with open(file, 'r') as f:
          
            data = json.load(f)
        if not data:
            print("No sales data found.")
            return  
        for sales in data:
            print(f"Item: {sales['item']}, Quantity: {sales['quantity']}, Date: {sales['date']}, Amount: {sales['amount']}, Total Amount: {sales['totalamount']}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file}'. Check file format.")


def sales_menu():
    while True:
        print("\n--- Sales Menu ---")
        print("1 for add sales")
        print("2 for view sales")
        print("3 for exit")

    
        choice = input("Enter your choice (1, 2, or 3): ")

        
        if choice == '1':
            print("Action: Add sales selected.")
        
        elif choice == '2':
              print("Action: View sales selected.")
        
        elif choice == '3':
            print("Action: Exiting program.")
            break  
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    sales_menu()


    