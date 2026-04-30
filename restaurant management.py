import tkinter as tk 
from tkinter import ttk , messagebox 
class RestuarantApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Restuarant Management System")
        self.root.geometry("500x400")

        self.menu = {
            "fries meal":2,
            "lunch meal":2,
            "burger meal":3,
            "pizza meal":4,
            "cheese burger meal":2.5,
            "drinks meal":1
        }
        
        self.rat=82
        self.entries = {}

        tk.Label(root, text="Restaurant order management", font=("Arial", 16, "bold")).pack(pady=10)
        frame = tk.Frame(root)
        frame.pack()

        for item, price in self.menu.items():
            tk.Label(frame, text=f"{item} (${price})").pack()
            entry = tk.Entry(frame, width=5)
            entry.pack()
            self.entries[item] = entry

        self.currency = tk.StringVar(value ="USD")
        ttk.Combobox(root,textvariable=self.currency,values=["USD","INR"],state="readonly").pack(pady=10)
        tk.Button(root, text="place order", command=self.place_order).pack(pady=10)

    def place_order(self):
        total= 0 
        symbol = "₹" if self.currency.get() == "INR" else "$"
        rate = self.rate if self.currency.get()=="INR" else 1
        summary = "order summary:\n"
        for item, entry in self.entries.items():
            q= entry.get()
            if q.isdigit() and int(q)>0:
                q = int(q)
                Cost= q * self.menu[item] * rate
                total += Cost
                summary += f"{item}: {q} x {symbol}{Cost}\n"
        if total:
            messagebox.showinfo("bill", summary+f"\nTotal: {symbol}{total}  ")
        else:
            messagebox.showerror("error", "order something")

root= tk.Tk()
app = RestuarantApp(root)
root.mainloop()
