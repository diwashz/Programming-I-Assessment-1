# Diwash Karki
# 20262356 Programming I Assessment
# Whitecliffe College, New Zealand

requisition_counter = 0


# Task 1

def add_requisition():
    global requisition_counter

    print("Enter your info -")

    date = input("Date - ").strip()
    while date == "":
        date = input("Date can't be blank, enter again ").strip()

    staff_id = input("Staff ID - ").strip()
    while staff_id == "":
        staff_id = input("Staff ID can't be blank, enter again ").strip()

    staff_name = input("Staff Name - ").strip()
    while staff_name == "":
        staff_name = input("Staff Name can't be blank, enter again ").strip()

    requisition_counter = requisition_counter + 1
    requisition_id = 10000 + requisition_counter
    print("Requisition ID -", requisition_id)

    print("\nAdd your Items -")
    items = []
    total = 0
    decision = "yes"

    while decision == "yes":
        item_name = input("Item Name - ").strip()
        while item_name == "":
            item_name = input("Item Name can't be blank, enter again ").strip()

        item_price = 0
        while item_price <= 0:
            try:
                item_price = float(input("Item Price (in $) - "))
                if item_price <= 0:
                    print("Price must be more than zero.")
            except ValueError:
                print("Price must be a number.")
                item_price = 0

        items.append([item_name, item_price])
        total = total + item_price

        decision = input("Add Another Item? (yes or no) ").strip().lower()
        while decision != "yes" and decision != "no":
            decision = input("Please type either yes or no ").strip().lower()

    print("Total - $" + str(total))

    requisition = {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id,
        "items": items,
        "total": total,
        "status": "Pending",
        "approval_ref": "Not Available",
    }
    return requisition


# Task 2

def requisition_approval(requisition):
    status = "Pending"
    approval_ref = "Not Available"

    if requisition["total"] < 500:
        status = "Approved"
        approval_ref = requisition["staff_id"] + str(requisition["requisition_id"])[-3:]

    requisition["status"] = status
    requisition["approval_ref"] = approval_ref

    print("Total - $" + str(requisition["total"]))
    print("Status -", status)
    print("Approval Number -", approval_ref)
    return requisition


# Task 3

def display_requisitions(all_requisitions):
    print("\nRequisitions -")

    if all_requisitions == []:
        print("No Requisitions -")
        return

    for requisition in all_requisitions:
        print("Date -", requisition["date"])
        print("Requisition ID -", requisition["requisition_id"])
        print("Staff ID -", requisition["staff_id"])
        print("Staff Name -", requisition["staff_name"])
        print("Total - $" + str(requisition["total"]))
        print("Status -", requisition["status"])
        print("Approval Number -", requisition["approval_ref"])
        print()



choice = input("Type 1 for Console or 2 for GUI - ").strip()
while choice != "1" and choice != "2":
    choice = input("Please type either 1 or 2 ").strip()

\
if choice == "1":
    all_requisitions = []
    another = "yes"

    while another == "yes":
        requisition = add_requisition()
        requisition_approval(requisition)
        all_requisitions.append(requisition)

        another = input("Add Another Requisition? (yes or no) ").strip().lower()
        while another != "yes" and another != "no":
            another = input("Please type either yes or no ").strip().lower()

    display_requisitions(all_requisitions)


# Task 4

import tkinter as tk


def gui():
    gui_items = []

    window = tk.Tk()
    window.title("Purchase Requisition System")
    window.geometry("400x560")

    entries = {}
    for name in ["Date", "Staff ID", "Staff Name", "Item Name", "Item Price"]:
        tk.Label(window, text=name + " -").pack()
        entries[name] = tk.Entry(window)
        entries[name].pack()

    items_box = tk.Listbox(window, height=5, width=35)
    items_box.pack(pady=5)

    output = tk.Label(window, text="")
    output.pack(pady=10)

    def get_total():
        total = 0
        for item in gui_items:
            total = total + item["price"]
        return total

    def add_item():
        item_name = entries["Item Name"].get().strip()
        if item_name == "":
            output.config(text="Item Name can't be blank, enter again")
            return

        try:
            price = float(entries["Item Price"].get())
            if price <= 0:
                raise ValueError
        except ValueError:
            output.config(text="Price must be a number more than zero")
            return

        gui_items.append({"name": item_name, "price": price})
        items_box.insert(tk.END, item_name + " - $" + str(price))
        output.config(text="Item Added - " + item_name)
        entries["Item Name"].delete(0, tk.END)
        entries["Item Price"].delete(0, tk.END)

    def calculate_total():
        if gui_items == []:
            output.config(text="Add at least one Item first")
            return
        output.config(text=f"Total - ${get_total():.2f}")

    def check_approval():
        global requisition_counter

        date = entries["Date"].get().strip()
        staff_id = entries["Staff ID"].get().strip()
        staff_name = entries["Staff Name"].get().strip()

        if date == "" or staff_id == "" or staff_name == "":
            output.config(text="Please Fill in All Details")
            return
        if gui_items == []:
            output.config(text="Add at least one Item first")
            return

        requisition_counter = requisition_counter + 1
        requisition = {
            "date": date,
            "staff_id": staff_id,
            "staff_name": staff_name,
            "requisition_id": 10000 + requisition_counter,
            "items": list(gui_items),
            "total": get_total(),
            "status": "Pending",
            "approval_ref": "Not Available",
        }
        requisition_approval(requisition)

        output.config(
            text=f"Total - ${requisition['total']:.2f}\n"
                 f"Status - {requisition['status']}\n"
                 f"Approval Number - {requisition['approval_ref']}"
        )
        gui_items.clear()
        items_box.delete(0, tk.END)

    tk.Button(window, text="Add Item", command=add_item).pack()
    tk.Button(window, text="Calculate Total", command=calculate_total).pack()
    tk.Button(window, text="Check Approval", command=check_approval).pack()

    window.mainloop()


if choice == "2":
    gui()