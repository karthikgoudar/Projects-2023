import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hospital Management System")

# Create a patient frame to store patient information
patient_frame = tk.LabelFrame(root, text="Patient Information")
patient_frame.grid(row=0, column=0, padx=10, pady=10)

# Add labels and entry widgets to the patient frame
tk.Label(patient_frame, text="Patient Name").grid(row=0, column=0, padx=5, pady=5)
patient_name_entry = tk.Entry(patient_frame)
patient_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(patient_frame, text="Patient Age").grid(row=1, column=0, padx=5, pady=5)
patient_age_entry = tk.Entry(patient_frame)
patient_age_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(patient_frame, text="Patient Gender").grid(row=2, column=0, padx=5, pady=5)
patient_gender_entry = tk.Entry(patient_frame)
patient_gender_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a patient info display area
display_frame = tk.LabelFrame(root, text="Patient Info")
display_frame.grid(row=1, column=0, padx=10, pady=10)

display_text = tk.Text(display_frame, height=10, width=30)
display_text.grid(row=0, column=0, padx=5, pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=lambda: submit_patient_info(patient_name_entry.get(), patient_age_entry.get(), patient_gender_entry.get()))
submit_button.grid(row=2, column=0, padx=10, pady=10)

def submit_patient_info(name, age, gender):
    display_text.insert("1.0", f"Name: {name}\n")
    display_text.insert("2.0", f"Age: {age}\n")
    display_text.insert("3.0", f"Gender: {gender}\n")

# Run the main loop
root.mainloop()
