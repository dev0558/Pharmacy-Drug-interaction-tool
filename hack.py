import tkinter as tk
from tkinter import ttk, messagebox

# Dataset
disease_to_medicines = {
    "Headache": ["Paracetamol", "Ibuprofen", "Aspirin"],
    "Depression": ["Fluoxetine (Prozac)", "Sertraline", "St. John’s Wort"],
    "Hypertension": ["Lisinopril", "Amlodipine", "Losartan"],
    "Diabetes": ["Metformin", "Insulin", "Glipizide"],
    "Allergies": ["Antihistamines", "Loratadine", "Cetirizine"],
    "Cholesterol": ["Atorvastatin (Lipitor)", "Rosuvastatin", "Simvastatin"],
}

food_interactions = {
    "Paracetamol": {"Alcohol": "May increase liver toxicity.", "Caffeine": "May reduce the effect."},
    "Ibuprofen": {"Coffee": "May cause stomach irritation.", "Alcohol": "Increases risk of ulcers."},
    "Aspirin": {"Grapefruit": "Increases toxicity risk.", "Garlic": "Increases bleeding risk."},
    "Fluoxetine (Prozac)": {"Caffeine": "May cause nervousness and heart palpitations."},
    "St. John’s Wort": {"Antidepressants": "Risk of serotonin syndrome.", "Birth Control": "May reduce effectiveness."},
    "Lisinopril": {"Bananas": "Can cause irregular heart rhythms due to high potassium.", "Salt Substitutes": "Risk of high potassium."},
    "Metformin": {"Alcohol": "May cause lactic acidosis.", "High-Fat Meals": "May delay absorption."},
    "Insulin": {"Cinnamon": "May cause excessive blood sugar drops.", "Alcohol": "Increases hypoglycemia risk."},
    "Atorvastatin (Lipitor)": {"Grapefruit": "Can increase statin levels, leading to toxicity.", "Alcohol": "Increases liver damage risk."},
}

# Function to handle search logic
def check_interactions():
    user_input = input_entry.get().strip()
    if not user_input:
        messagebox.showwarning("Input Required", "Please enter a medicine or select a disease.")
        return

    result_window = tk.Toplevel(root)
    result_window.title("Interaction Results")
    result_window.geometry("400x400")
    result_window.configure(bg="#f4f4f4")

    result_label = tk.Label(result_window, text="Results:", font=("Arial", 14, "bold"), bg="#f4f4f4")
    result_label.pack(pady=10)

    result_frame = tk.Frame(result_window, bg="#ffffff", relief="sunken", borderwidth=2)
    result_frame.pack(pady=10, padx=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(result_frame)
    scrollbar.pack(side="right", fill="y")

    result_text = tk.Text(result_frame, wrap="word", yscrollcommand=scrollbar.set, bg="#ffffff", font=("Arial", 12))
    result_text.pack(fill="both", expand=True)
    scrollbar.config(command=result_text.yview)

    # Check if input is a disease
    if user_input in disease_to_medicines:
        medicines = disease_to_medicines[user_input]
        result_text.insert(tk.END, f"Disease: {user_input}\n\n")
        result_text.insert(tk.END, "Recommended Medicines and Interactions:\n")
        for med in medicines:
            result_text.insert(tk.END, f"\nMedicine: {med}\n")
            interactions = food_interactions.get(med, {})
            if interactions:
                for item, effect in interactions.items():
                    result_text.insert(tk.END, f"  - {item}: {effect}\n")
            else:
                result_text.insert(tk.END, "  No known interactions.\n")
    else:  # Check if input is a medicine
        interactions = food_interactions.get(user_input, None)
        if interactions:
            result_text.insert(tk.END, f"Medicine: {user_input}\n\nInteractions:\n")
            for item, effect in interactions.items():
                result_text.insert(tk.END, f"  - {item}: {effect}\n")
        else:
            result_text.insert(tk.END, f"No known interactions for '{user_input}'.")

    result_text.config(state="disabled")  # Make text read-only

# Initialize main window
root = tk.Tk()
root.title("Pharmacy Drug Interaction Tool")
root.geometry("500x400")
root.configure(bg="#e3f2fd")

# Header
header = tk.Label(root, text="Pharmacy Drug Interaction Tool", font=("Arial", 18, "bold"), bg="#2196F3", fg="#ffffff")
header.pack(pady=10, fill="x")

# Input field
input_frame = tk.Frame(root, bg="#e3f2fd")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter Medicine or Disease:", font=("Arial", 12), bg="#e3f2fd")
input_label.grid(row=0, column=0, padx=5)

input_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
input_entry.grid(row=0, column=1, padx=5)

# Dropdown for diseases
dropdown_label = tk.Label(input_frame, text="Or Select a Disease:", font=("Arial", 12), bg="#e3f2fd")
dropdown_label.grid(row=1, column=0, padx=5)

selected_disease = tk.StringVar()
disease_dropdown = ttk.Combobox(input_frame, textvariable=selected_disease, values=list(disease_to_medicines.keys()), font=("Arial", 12), state="readonly")
disease_dropdown.grid(row=1, column=1, padx=5, pady=5)

def on_disease_select(event):
    input_entry.delete(0, tk.END)
    input_entry.insert(0, selected_disease.get())

disease_dropdown.bind("<<ComboboxSelected>>", on_disease_select)

# Search button
search_button = tk.Button(root, text="Check Interactions", font=("Arial", 12), bg="#4CAF50", fg="#ffffff", command=check_interactions)
search_button.pack(pady=10)

# Footer
footer = tk.Label(root, text="Powered by Team CyberSecurity", font=("Arial", 10), bg="#e3f2fd", fg="#777777")
footer.pack(side="bottom", pady=10)

root.mainloop()
