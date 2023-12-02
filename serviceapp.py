import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import os
from os import path
from tkinter.tix import IMAGETEXT



bt_height = 3
bt_width = 15



    
	


# Function to display text file contents
def display_text_file(file_path):
    try:
        with open(file_path, "r") as file:
            file_contents = file.read()

            text_window = tk.Tk()
            text_window.title("Text File Contents")

            text_area = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=40, height=20)
            text_area.insert("1.0", file_contents)
            text_area.config(state="disabled")
            text_area.pack()

            text_window.mainloop()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found: " + file_path)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))


customer_address_entry = ''
customer_name_entry = ''
date_entry = ''
report_text = ''
rodenticide_entry = ''
recommendations_text = ''
follow_up_entry = ''
# Function to save a report to a text file
def save_report():
    
    
    customer_name = customer_name_entry
    customer_address = customer_address_entry
    date = date_entry
    report = report_text
    rodenticide = rodenticide_entry
    recommendations = recommendations_text
    follow_up = follow_up_entry

    file_name = f'{customer_name}.txt'
    
    try:
        with open(file_name, "w") as file:
            file.write("Customer Name: " + customer_name + "\n")
            file.write("Customer Address: " + customer_address + "\n")
            file.write("Date: " + date + "\n")
            file.write("Report:\n" + report)
            file.write("Rodenticide used: " + rodenticide + "\n")
            file.write("Recommendations:\n" + recommendations)
            file.write("Follow up: " + follow_up + "\n")
        messagebox.showinfo("Success", "Report saved successfully as " + file_name)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while saving the report: " + str(e))

# Function to open the rodents submenu
def open_rodents_submenu():
    rodents_submenu = tk.Tk()
    rodents_submenu.title("Rodents Menu")
    
    rats_button = ttk.Button(rodents_submenu, text="Rats", command=lambda: display_text_file(os.path.join(os.getcwd(), "Rats.txt")))
    mice_button = ttk.Button(rodents_submenu, text="Mice", command=lambda: display_text_file(os.path.join(os.getcwd(), "Mice.txt")))
    
    rats_button.pack()
    mice_button.pack()
    
    rodents_submenu.mainloop()

# Create the main application window
app = tk.Tk()
app.title("Service Application")

# Load the background image


# Create the main screen
def show_main_screen():
    main_frame = ttk.Frame(app)
    main_frame.place(relx=0.5, rely=0.5, anchor="center",)
    contract_button = ttk.Button(main_frame, text="Contract", command=lambda: on_contract())
    report_button = ttk.Button(main_frame, text="Reports", command=lambda: on_report())
    pest_button = ttk.Button(main_frame, text="Pest", command=lambda: on_pest())
    contract_button.grid(column=0, row=0, pady=50)
    report_button.grid(column=1, row=0, pady=50)
    pest_button.grid(column=2, row=0, pady=50)

# Create the report form
def on_report():
    
    report_frame = ttk.Frame(app)
    report_frame.grid(column=0, row=0)
    customer_name_label = ttk.Label(report_frame, text="Customer Name:")
    customer_name_label.grid(column=0, row=0)
    customer_name_entry = ttk.Entry(report_frame)
    customer_name_entry.grid(column=1, row=0)
    customer_address_label = ttk.Label(report_frame, text="Customer Address:")
    customer_address_label.grid(column=0, row=1)
    customer_address_entry = ttk.Entry(report_frame)
    customer_address_entry.grid(column=1, row=1)
    date_label = ttk.Label(report_frame, text="Date:")
    date_label.grid(column=0, row=2)
    date_entry = ttk.Entry(report_frame)
    date_entry.grid(column=1, row=2)
    report_label = ttk.Label(report_frame, text="Report:")
    report_label.grid(column=0, row=3)
    report_text = scrolledtext.ScrolledText(report_frame, wrap=tk.WORD, width=40, height=5)
    report_text.grid(column=1, row=3)
    rodenticide_label = ttk.Label(report_frame, text="Rodenticide used:")
    rodenticide_label.grid(column=0, row=4)
    rodenticide_entry = ttk.Entry(report_frame)
    rodenticide_entry.grid(column=1, row=4)
    recommendations_label = ttk.Label(report_frame, text="Recommendations:")
    recommendations_label.grid(column=0, row=5)
    recommendations_text = scrolledtext.ScrolledText(report_frame, wrap=tk.WORD, width=40, height=5)
    recommendations_text.grid(column=1, row=5)
    follow_up_label = ttk.Label(report_frame, text="Follow up:")
    follow_up_label.grid(column=0, row=6)
    follow_up_entry = ttk.Entry(report_frame)
    follow_up_entry.grid(column=1, row=6)
    save_button = ttk.Button(report_frame, text="Save Report", command=lambda: save_report())
    save_button.grid(column=1, row=7)

# Create the pest screen
def on_pest():
    pest_frame = ttk.Frame(app)
    pest_frame.grid(column=0, row=0)
    birds_button = ttk.Button(pest_frame, text="Birds")
    rodents_button = ttk.Button(pest_frame, text="Rodents", command=lambda: open_rodents_submenu())
    insects_button = ttk.Button(pest_frame, text="Insects")
    birds_button.grid(column=0, row=0)
    rodents_button.grid(column=1, row=0)
    insects_button.grid(column=2, row=0)
    
def on_contract():
    pass



# Start with the main screen
show_main_screen()

app.mainloop()

