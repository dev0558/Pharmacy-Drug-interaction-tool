import tkinter as tk
from tkinter import ttk, messagebox


disease_to_medicines = {
    "Headache": ["Paracetamol", "Ibuprofen", "Aspirin"],
    "Depression": ["Fluoxetine (Prozac)", "Sertraline", "St. John's Wort"],
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
    "St. John's Wort": {"Antidepressants": "Risk of serotonin syndrome.", "Birth Control": "May reduce effectiveness."},
    "Lisinopril": {"Bananas": "Can cause irregular heart rhythms due to high potassium.", "Salt Substitutes": "Risk of high potassium."},
    "Metformin": {"Alcohol": "May cause lactic acidosis.", "High-Fat Meals": "May delay absorption."},
    "Insulin": {"Cinnamon": "May cause excessive blood sugar drops.", "Alcohol": "Increases hypoglycemia risk."},
    "Atorvastatin (Lipitor)": {"Grapefruit": "Can increase statin levels, leading to toxicity.", "Alcohol": "Increases liver damage risk."},
}

def show_visualization():
    vis_window = tk.Toplevel(root)
    vis_window.title("Medicine Interactions Visualization")
    vis_window.geometry("800x600")
    
    canvas = tk.Canvas(vis_window, width=800, height=600, bg='white')
    canvas.pack(fill="both", expand=True)
    
    # Draw title
    canvas.create_text(400, 40, text="Medicine and Food Interactions", 
                      font=("Arial", 20, "bold"), fill="#2196F3")
    
    # Draw medicines (left side)
    medicines = ["Paracetamol", "Ibuprofen", "Aspirin"]
    med_y_positions = [150, 300, 450]
    med_x = 200
    
    for med, y in zip(medicines, med_y_positions):
        # Draw medicine circle
        canvas.create_oval(med_x-50, y-50, med_x+50, y+50, 
                         fill="#4CAF50", outline="")
        canvas.create_text(med_x, y, text=med, fill="white", 
                         font=("Arial", 12))
        
        # Draw interactions for each medicine
        if med in food_interactions:
            foods = list(food_interactions[med].keys())
            for i, food in enumerate(foods):
                food_y = y - 30 + i * 60
                food_x = 600
                
                # Draw food circle
                canvas.create_oval(food_x-40, food_y-40, food_x+40, food_y+40,
                                 fill="#ff5722", outline="")
                canvas.create_text(food_x, food_y, text=food, fill="white",
                                 font=("Arial", 12))
                
                # Draw connection line
                canvas.create_line(med_x+50, y, food_x-40, food_y,
                                 fill="#ff9800", width=2)
    
    # Draw legend
    legend_y = 550
    # Medicine legend
    canvas.create_oval(50, legend_y-10, 70, legend_y+10, fill="#4CAF50", outline="")
    canvas.create_text(100, legend_y, text="Medicines", anchor="w")
    # Food legend
    canvas.create_oval(150, legend_y-10, 170, legend_y+10, fill="#ff5722", outline="")
    canvas.create_text(200, legend_y, text="Food/Substances", anchor="w")
    # Interaction legend
    canvas.create_line(300, legend_y, 340, legend_y, fill="#ff9800", width=2)
    canvas.create_text(370, legend_y, text="Interaction", anchor="w")

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
    else:
        interactions = food_interactions.get(user_input, None)
        if interactions:
            result_text.insert(tk.END, f"Medicine: {user_input}\n\nInteractions:\n")
            for item, effect in interactions.items():
                result_text.insert(tk.END, f"  - {item}: {effect}\n")
        else:
            result_text.insert(tk.END, f"No known interactions for '{user_input}'.")

    result_text.config(state="disabled")

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

# Button frame
button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

# Search button
search_button = tk.Button(button_frame, text="Check Interactions", font=("Arial", 12), bg="#4CAF50", fg="#ffffff", command=check_interactions)
search_button.pack(side="left", padx=5)

# Visualization button
vis_button = tk.Button(button_frame, text="Show Visualization", font=("Arial", 12), bg="#2196F3", fg="#ffffff", command=show_visualization)
vis_button.pack(side="left", padx=5)

# Footer
footer = tk.Label(root, text="Powered by Team CyberSecurity", font=("Arial", 10), bg="#e3f2fd", fg="#777777")
footer.pack(side="bottom", pady=10)

root.mainloop()
