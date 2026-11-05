# Name: Diwash
# hi
requisition_counter = 0


# Task 1

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




# Task 2

def requisition_approval(requisition):
    """Approve automatically if the total is less than $500 and keep pending if not"""
    requisition["status"] = "Pending"
    requisition["approval_ref"] = "N/A"

    if requisition["total"] < 500:
        requisition["status"] = "Approved"
        requisition["approval_ref"] = (
            requisition["staff_id"] + str(requisition["requisition_id"])[-3:]
        )

    print(f"Total: ${requisition['total']:g}")
    print(f"Status: {requisition['status']}")
    print("Approval Reference Number:", requisition["approval_ref"])
    return requisition

req = add_requisition()
requisition_approval(req)


# Task 3

def display_requisitions(all_requisitions):
    """Print basic info, total and approval details."""
    print("\nPrinting requisitions:")
    if len(all_requisitions) == 0: 
        print("No requisitions.")
        return 

    for req in all_requisitions: 
        print("Date:", req["date"])
        print("Requisition ID: ", req["requisition_id"])
        print("Staff ID:", req["staff_id"])
        print("Staff Name:", req["staff_name"])
        print(f"Total ${req["total"]:g}")
        print("Status:", req["status"])
        print("\nApproval Reference Number:", req["approval_ref"])
        print()
        