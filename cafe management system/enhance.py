import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk  # Requires: pip install pillow
import os

menus = {
    "Pizza": 230,
    "Momo": 110,
    "Burger": 150,
    "Chicken Wings": 220,
    "Biryani": 300,
    "Naam": 120,
}

order_details = {}

def update_order(item, qty_entry):
    try:
        qty = int(qty_entry.get())
        if qty <= 0:
            raise ValueError
        order_details[item] = order_details.get(item, 0) + qty
        messagebox.showinfo("Order Updated", f"{item} x{qty} added to your order.")
    except ValueError:
        messagebox.showerror("Invalid Quantity", "Please enter a valid positive integer.")

def reset_order():
    if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset your order?"):
        order_details.clear()
        messagebox.showinfo("Reset", "Your order has been cleared.")

def save_and_print_bill(bill_text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(bill_text)
        try:
            os.startfile(file_path, "print")
            messagebox.showinfo("Print", "Bill sent to printer.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to print: {e}")

def show_bill():
    if not order_details:
        messagebox.showwarning("No Order", "No items ordered.")
        return

    bill_window = tk.Toplevel(root)
    bill_window.title("Final Bill")
    tk.Label(bill_window, text="🧾 FINAL BILL 🧾", font=("Arial", 16, "bold")).pack(pady=5)

    bill_text_widget = tk.Text(bill_window, width=40, height=18)
    bill_text_widget.pack()

    total = 0
    bill_text = f"{'Item':<15}{'Qty':<5}{'Total':<10}\n"
    bill_text += "-" * 35 + "\n"
    for item, qty in order_details.items():
        item_total = menus[item] * qty
        bill_text += f"{item:<15}{qty:<5}{item_total:<10}\n"
        total += item_total
    bill_text += "-" * 35 + "\n"
    bill_text += f"{'TOTAL':<20}Rs {total}\n"
    bill_text += "🙏 Thank you for ordering with us 🙏\n"

    bill_text_widget.insert(tk.END, bill_text)

    # QR Code Image (mock UPI payment QR)
    qr_frame = tk.Frame(bill_window)
    qr_frame.pack(pady=5)

    try:
        qr_img = Image.open("qr_payment.png")  # Use your actual QR code image file here
        qr_img = qr_img.resize((150, 150))
        qr_photo = ImageTk.PhotoImage(qr_img)
        tk.Label(qr_frame, text="Scan to Pay via UPI").pack()
        tk.Label(qr_frame, image=qr_photo).pack()
        qr_frame.image = qr_photo  # prevent garbage collection
    except FileNotFoundError:
        tk.Label(qr_frame, text="🔴 QR code image 'qr_payment.png' not found").pack()

    # Save and Print Button
    btn_frame = tk.Frame(bill_window)
    btn_frame.pack(pady=10)
    tk.Button(btn_frame, text="🖨️ Save & Print Bill", command=lambda: save_and_print_bill(bill_text)).pack()

# --- GUI Setup ---
root = tk.Tk()
root.title("🍽️ Menu Ordering System")

tk.Label(root, text="🍽️ MENU CARD 🍽️", font=("Arial", 18, "bold")).pack(pady=10)

menu_frame = tk.Frame(root)
menu_frame.pack()

for item, price in menus.items():
    row = tk.Frame(menu_frame)
    row.pack(pady=2)

    tk.Label(row, text=f"{item} - Rs {price}", width=25, anchor='w').pack(side=tk.LEFT)
    qty_entry = tk.Entry(row, width=5)
    qty_entry.pack(side=tk.LEFT)
    tk.Button(row, text="Add", command=lambda i=item, q=qty_entry: update_order(i, q)).pack(side=tk.LEFT)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Show Bill", command=show_bill, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Reset Order", command=reset_order, width=15).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Exit", command=root.quit, width=15).grid(row=0, column=2, padx=5)

root.mainloop()
