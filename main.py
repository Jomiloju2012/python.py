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


def read_json_file(filepath):

    try:
       
        with open(file, 'r') as file:
          
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file}'. Check file format.")
        return None

file_content = read_json_file('data.json')
if file_content:
    print("Successfully loaded data:")
    print(file_content)
    print(f"Name: {file_content.get('name')}")




    