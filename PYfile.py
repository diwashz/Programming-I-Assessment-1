# Diwash Karki
# 20262356 Programming I Assessment 
# Whitecliffe College, New Zealand
#

import tkinter as tk
 
requisition_counter = 0
 
 
# task 1
 
def add_requisition():
    """Collect staff info and items, generate ID and return everything."""
    global requisition_counter
 
    print("Enter your Info:")
    date = input("Date:").strip()
    while date == "":
        date = input("Date cannot be blank. Date:").strip()
 
    staff_id = input("Staff ID:").strip()
    while staff_id == "":
        staff_id = input("Staff ID cannot be blank. Staff ID:").strip()
 
    staff_name = input("Staff Name:").strip()
    while staff_name == "":
        staff_name = input("Staff Name cannot be blank. Staff Name:").strip()
 
    requisition_counter += 1
    requisition_id = 10000 + requisition_counter
    print("Requisition ID:", requisition_id)
 
    items = []
    print("\nAdd Items: ")
    while True:
        item_name = input("Item Name:").strip()
        while item_name == "":
            item_name = input("Item name cannot be blank. Item Name:").strip()
 
        while True:
            try:
                item_price = float(input("Item Price, $:").strip())
                if item_price <= 0:
                    print("Price must be above zero. Please try again.")
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
    print(f"Total: ${total:.2f}")
 
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
 
 
# task 2
 
def requisition_approval(requisition):
    """Approve automatically if the total is less than $500 and keep pending if not"""
    requisition["status"] = "Pending"
    requisition["approval_ref"] = "N/A"
 
    if requisition["total"] < 500:
        requisition["status"] = "Approved"
        requisition["approval_ref"] = (
            requisition["staff_id"] + str(requisition["requisition_id"])[-3:]
        )
 
    print(f"Total: ${requisition['total']:.2f}")
    print(f"Status: {requisition['status']}")
    print("Approval Reference Number:", requisition["approval_ref"])
    return requisition
 
 
# task 3
 
def display_requisitions(all_requisitions):
    """Print basic info, total and approval details."""
    print("\nPrinting requisitions:")
    if len(all_requisitions) == 0:
        print("No requisitions.")
        return
 
    for req in all_requisitions:
        print("Date:", req["date"])
        print("Requisition ID:", req["requisition_id"])
        print("Staff ID:", req["staff_id"])
        print("Staff Name:", req["staff_name"])
        print(f"Total ${req['total']:.2f}")
        print("Status:", req["status"])
        print("Approval Reference Number:", req["approval_ref"])
        print()
 
 
# task 4
 
def run_gui():
    window = tk.Tk()
    window.title("Purchase Requisition System")
 
    gui_items = []
    entries = {}
    for name in ["Date", "Staff ID", "Staff Name", "Item Name", "Item Price"]:
        tk.Label(window, text=name + ":").pack()
        entries[name] = tk.Entry(window)
        entries[name].pack()
 
    output = tk.Label(window, text="")
    output.pack(pady=10)
 
    def get_total():
        total = 0
        for item in gui_items:
            total += item["price"]
        return total
 
    def add_item():
        item_name = entries["Item Name"].get().strip()
        try:
            price = float(entries["Item Price"].get())
            if price <= 0:
                raise ValueError
        except ValueError:
            output.config(text="Please enter a valid price above zero")
            return
        if item_name == "":
            output.config(text="Please enter an item name")
            return
 
        gui_items.append({"name": item_name, "price": price})
        output.config(text=f"Items added: {len(gui_items)}")
        entries["Item Name"].delete(0, tk.END)
        entries["Item Price"].delete(0, tk.END)
 
    def calculate_total():
        if len(gui_items) == 0:
            output.config(text="Add at least one item first")
            return
        output.config(text=f"Total: ${get_total():.2f}")
 
    def check_approval():
        global requisition_counter
 
        date = entries["Date"].get().strip()
        staff_id = entries["Staff ID"].get().strip()
        staff_name = entries["Staff Name"].get().strip()
        if date == "" or staff_id == "" or staff_name == "":
            output.config(text="Please fill in Date, Staff ID and Staff Name")
            return
        if len(gui_items) == 0:
            output.config(text="Add at least one item first")
            return
 
        requisition_counter += 1
        requisition = {
            "date": date,
            "staff_id": staff_id,
            "staff_name": staff_name,
            "requisition_id": 10000 + requisition_counter,
            "items": list(gui_items),
            "total": get_total(),
            "status": "Pending",
            "approval_ref": "N/A",
        }
        requisition_approval(requisition)
 
        output.config(
            text=f"Total: ${requisition['total']:.2f}\n"
                 f"Status: {requisition['status']}\n"
                 f"Approval Reference Number: {requisition['approval_ref']}"
        )
        gui_items.clear()
 
    tk.Button(window, text="Add Item", command=add_item).pack()
    tk.Button(window, text="Calculate Total", command=calculate_total).pack()
    tk.Button(window, text="Check Approval", command=check_approval).pack()
 
    window.mainloop()
 
 
def main():
    all_requisitions = []
 
    choice = input("Type 1 for console version or 2 for GUI: ").strip()
 
    if choice == "1":
        while True:
            req = add_requisition()
            requisition_approval(req)
            all_requisitions.append(req)
 
            another = input("Add another requisition? (yes/no): ").strip().lower()
            while another not in ("yes", "no"):
                another = input("Please answer 'yes' or 'no': ").strip().lower()
            if another == "no":
                break
 
        display_requisitions(all_requisitions)
    elif choice == "2":
        run_gui()
    else:
        print("Invalid choice")
 
 
main()
