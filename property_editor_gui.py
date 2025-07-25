

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import glob

def process_files():
    folder_path = folder_path_var.get()
    file_pattern = file_name_var.get()
    property_name = property_name_var.get()
    new_value = property_value_var.get()
    missing_action = missing_property_action_var.get()

    if not all([folder_path, file_pattern, property_name, new_value]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", f"Folder not found: {folder_path}")
        return

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, f"Processing files in: {folder_path}\n")
    output_text.insert(tk.END, f"File pattern: {file_pattern}\n")
    output_text.insert(tk.END, f"Action for missing properties: {missing_action}\n")
    output_text.insert(tk.END, "-------------------------------------\n")

    search_path = os.path.join(folder_path, file_pattern)
    files_to_process = glob.glob(search_path)

    if not files_to_process:
        output_text.insert(tk.END, "No files found matching the pattern.\n")
        return

    for file_path in files_to_process:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            property_found = False
            updated_lines = []
            value_changed = False

            for line in lines:
                stripped_line = line.strip()
                if stripped_line.startswith(property_name):
                    property_found = True
                    parts = stripped_line.split('=', 1)
                    if len(parts) == 2 and parts[0].strip() == property_name:
                        current_value = parts[1].strip()
                        if current_value != new_value:
                            updated_lines.append(f"{property_name} = {new_value}\n")
                            value_changed = True
                            output_text.insert(tk.END, f"Updating property in {os.path.basename(file_path)}\n")
                        else:
                            updated_lines.append(line)
                            output_text.insert(tk.END, f"Value is already correct in {os.path.basename(file_path)}. Skipping.\n")
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)

            if not property_found:
                add_prop = False
                if missing_action == "ask":
                    add_prop = messagebox.askyesno(
                        "Property Not Found",
                        f"The property '{property_name}' was not found in {os.path.basename(file_path)}.\n\nDo you want to add it?"
                    )
                elif missing_action == "add":
                    add_prop = True
                # If missing_action is "skip", add_prop remains False

                if add_prop:
                    if updated_lines and not updated_lines[-1].endswith('\n'):
                        updated_lines.append('\n')
                    updated_lines.append(f"{property_name} = {new_value}\n")
                    value_changed = True
                    output_text.insert(tk.END, f"Adding new property to {os.path.basename(file_path)}\n")
                else:
                    output_text.insert(tk.END, f"Skipping file {os.path.basename(file_path)} as requested.\n")

            if value_changed:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(updated_lines)

        except Exception as e:
            output_text.insert(tk.END, f"Error processing {os.path.basename(file_path)}: {e}\n")

    output_text.insert(tk.END, "-------------------------------------\n")
    output_text.insert(tk.END, "Processing complete.\n")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

# --- GUI Setup ---
root = tk.Tk()
root.title("Property File Editor")

style = ttk.Style(root)
style.theme_use('clam')
style.configure("TLabel", padding=5, font=('Segoe UI', 10))
style.configure("TEntry", padding=5, font=('Segoe UI', 10))
style.configure("TButton", padding=5, font=('Segoe UI', 10, 'bold'))
style.configure("TLabelframe.Label", font=('Segoe UI', 10, 'bold'))

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --- Variables ---
folder_path_var = tk.StringVar()
file_name_var = tk.StringVar(value="Company_*.properties")
property_name_var = tk.StringVar()
property_value_var = tk.StringVar()
missing_property_action_var = tk.StringVar(value="ask") # Default action

# --- Input Widgets ---
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Folder Path:").grid(row=0, column=0, sticky=tk.W)
folder_entry = ttk.Entry(input_frame, textvariable=folder_path_var, width=50)
folder_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
browse_button = ttk.Button(input_frame, text="Browse...", command=browse_folder)
browse_button.grid(row=0, column=2, padx=(5,0))

ttk.Label(input_frame, text="File Name/Pattern:").grid(row=1, column=0, sticky=tk.W)
file_name_entry = ttk.Entry(input_frame, textvariable=file_name_var, width=50)
file_name_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="Property Name:").grid(row=2, column=0, sticky=tk.W)
property_name_entry = ttk.Entry(input_frame, textvariable=property_name_var, width=50)
property_name_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(input_frame, text="New Property Value:").grid(row=3, column=0, sticky=tk.W)
property_value_entry = ttk.Entry(input_frame, textvariable=property_value_var, width=50)
property_value_entry.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E))

input_frame.columnconfigure(1, weight=1)

# --- Action Frame ---
action_frame = ttk.LabelFrame(main_frame, text="Action for Missing Property", padding="10 10 10 10")
action_frame.grid(row=1, column=0, columnspan=3, pady=(10,0), sticky=(tk.W, tk.E))

ttk.Radiobutton(action_frame, text="Ask for each file", variable=missing_property_action_var, value="ask").pack(anchor=tk.W)
ttk.Radiobutton(action_frame, text="Automatically add property", variable=missing_property_action_var, value="add").pack(anchor=tk.W)
ttk.Radiobutton(action_frame, text="Skip files where property is missing", variable=missing_property_action_var, value="skip").pack(anchor=tk.W)

# --- Process Button ---
process_button = ttk.Button(main_frame, text="Process Files", command=process_files)
process_button.grid(row=2, column=1, columnspan=2, pady=(10,0), sticky=tk.E)

# --- Output Text Box ---
output_frame = ttk.LabelFrame(main_frame, text="Output", padding=5)
output_frame.grid(row=3, column=0, columnspan=3, pady=(10,0), sticky=(tk.W, tk.E, tk.N, tk.S))
output_text = tk.Text(output_frame, height=15, width=80, font=('Consolas', 9))
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text['yscrollcommand'] = scrollbar.set

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(3, weight=1)

root.mainloop()
