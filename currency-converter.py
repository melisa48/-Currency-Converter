import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime
from functools import lru_cache

class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        self.data = self.get_exchange_rates()
        self.currencies = self.data['rates']

    @lru_cache(maxsize=128)
    def get_exchange_rates(self, date=None):
        try:
            if date:
                url = f"{self.url}/{date}"
            else:
                url = self.url
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"API request failed: {e}")
            return None

    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.currencies or to_currency not in self.currencies:
            messagebox.showerror("Error", "Invalid currency code")
            return None

        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        converted_amount = round(amount * self.currencies[to_currency], 4)
        return converted_amount

def main():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    converter = CurrencyConverter(url)

    def perform_conversion():
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        try:
            amount = float(amount_entry.get())
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for amount")
            return

        converted_amount = converter.convert(from_currency, to_currency, amount)
        if converted_amount is not None:
            result_label.config(text=f"Converted Amount: {converted_amount} {to_currency}")

    def swap_currencies():
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        from_currency_var.set(to_currency)
        to_currency_var.set(from_currency)

    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("400x300")  # Set window size to 400x300

    font_style = ("Arial", 14)  # Set a larger font size

    from_currency_var = tk.StringVar(root)
    to_currency_var = tk.StringVar(root)
    from_currency_var.set("USD")
    to_currency_var.set("EUR")

    tk.Label(root, text="Amount:", font=font_style).grid(row=0, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(root, font=font_style)
    amount_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="From:", font=font_style).grid(row=1, column=0, padx=10, pady=10)
    from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=list(converter.currencies.keys()), font=font_style)
    from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="To:", font=font_style).grid(row=2, column=0, padx=10, pady=10)
    to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=list(converter.currencies.keys()), font=font_style)
    to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

    convert_button = tk.Button(root, text="Convert", command=perform_conversion, font=font_style)
    convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    swap_button = tk.Button(root, text="Swap", command=swap_currencies, font=font_style)
    swap_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    result_label = tk.Label(root, text="", font=font_style)
    result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
