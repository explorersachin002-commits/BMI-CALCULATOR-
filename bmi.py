import tkinter as tk
from tkinter import messagebox
import csv
import os

FILE_NAME = "bmi_data.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Weight", "Height", "BMI", "Category"])


def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, weight, height, f"{bmi:.2f}", category])

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def show_history():
    history = ""

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            history += f"Name: {row[0]} | BMI: {row[3]} | {row[4]}\n"

    if history == "":
        history = "No records found."

    messagebox.showinfo("BMI History", history)


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")

tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

tk.Button(root, text="View History", command=show_history).pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()