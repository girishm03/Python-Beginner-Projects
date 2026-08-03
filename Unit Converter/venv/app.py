import tkinter as tk
from tkinter import ttk


def length_convertor(value, from_unit, to_unit):
    # Conversion factors
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def convert_unit():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()
        if category == "Length":
            result = length_convertor(value, from_unit, to_unit)
        else:
            result = "Unsupported category."
        
        label_result.config(text=f"{value} {from_unit} is {result} {to_unit}")
            
    except ValueError:
        label_result.config(text="Please enter a valid number.")
        
root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x500")

#dropdown category
label_category = tk.Label(root, text="Select Category")
label_category.pack(pady=5)
combo_category = ttk.Combobox(root, values=["Length"], state="readonly")
combo_category.pack(pady=5)

#Convert from
label_category = tk.Label(root, text="Convert: ")
label_category.pack(pady=5)
combo_from = ttk.Combobox(root, values=["meters","kilometers","centimeters","millimeters","miles","yards","feet","inches"], state="readonly")
combo_from.pack(pady=5)

#convert to
label_category = tk.Label(root, text="convert to:")
label_category.pack(pady=5)
combo_to  = ttk.Combobox(root, values=["meters","kilometers","centimeters","millimeters","miles","yards","feet","inches"], state="readonly")
combo_to.pack(pady=5)

#entry for value input
label_value = tk.Label(root, text="Enter value:")
label_value.pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

#convertion button
button_convert = tk.Button(root, text="Convert", command=convert_unit)
button_convert.pack(pady=10)

#label to display result
label_result = tk.Label(root, text="Result:", font=("Arial", 15))
label_result.pack(pady=20)

#run the application

root.mainloop()