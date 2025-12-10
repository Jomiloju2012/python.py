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

add_sales()

    