# Name: Diwash
# hi
requisition_counter = 0

def add_requisition():
    """Collect staff info and items, generate ID and return everything."""
    global requisition_counter

    print("Enter your Info:")
    date = input("Date:").strip()
    staff_id = input("Staff ID:").strip()
    staff_name = input("Staff Name:").strip()

    requisition_counter += 1
    requisition_id = 10000 + requisition_counter
    print("Requisition ID:", requisition_id)

    items = []
    print("\nAdd Items: ")
    while True:
        item_name = input("Item Name:").strip()
        while True:
            try:
                item_price = float(input("Item Price, $:").strip())
                if item_price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number for the price.")

        items.append({"name": item_name, "price": item_price})

        another = input("Add Another item? (yes/no):").strip().lower()
        while another not in ("yes", "no"):
            another = input("Please answer 'yes' or 'no':").strip().lower()
        if another == "no":
            break

    total = 0
    for item in items:
        total += item["price"]
    print(f"Total: ${total:g}")

    requisition = {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id,
        "items": items,
        "total": total,
        "status": "Pending",
        "approval_ref": "N/A",
    }

    return requisition

print(add_requisition())  