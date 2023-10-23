# FILE RENAMER
import os

def rename_files(directory, prefix):
    # List all file names in the directory
    file_list = os.listdir(directory)

    for file_name in file_list:
        # Construct new file name with prefix
        new_file_name = f"{prefix}{file_name}"
    
        # Construct the full path to the file and the new file name
        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")

# Replace this with the path to your directory
target_directory = "C:\\Users\\Kai\\OneDrive\\Documents\\Python Projects\\PythonBatchFileProcessing\\SampleText"


# IMAGE CONVERTER
from PIL import Image

def convert_images(directory, original_format, target_format):
    file_list = os.listdir(directory)

    for file_name in file_list:
        if file_name.endswith(original_format):
            img = Image.open(os.path.join(directory, file_name))
            file_name_without_extenstion = os.path.splitext(file_name)[0]
            new_file_name = f"{file_name_without_extenstion}.{target_format}"
            img.save(os.path.join(directory, new_file_name))
            print(f"Converted {file_name} to {new_file_name}")



# GUI INTERFACE
import tkinter as tk
from tkinter import filedialog

def choose_directory_for_rename():
    folder_selected = filedialog.askdirectory()
    rename_files(folder_selected, "sample_")

def choose_directory_for_convert():
    folder_selected = filedialog.askdirectory()
    original_format = original_format_entry.get()
    target_format = target_format_entry.get()
    convert_images(folder_selected, original_format, target_format)

# Create the main window
root = tk.Tk()
root.geometry('600x400')

# Add a button for renaming files
format_button = tk.Button(root, text="Rename Files", command=choose_directory_for_rename)
format_button.pack(pady=(20, 40))

# Add entry widgets to accept original and target image  formats
tk.Label(root, text="Original Format:").pack()
original_format_entry = tk.Entry(root)
original_format_entry.pack()
original_format_entry.insert(0, ".jpg")

tk.Label(root, text="Target Format:").pack()
target_format_entry = tk.Entry(root)
target_format_entry.pack()
target_format_entry.insert(0, ".png")

# Add a button for converting images
convert_button = tk.Button(root, text="Convert Images", command=choose_directory_for_convert)
convert_button.pack(pady=(20, 20))

# Start the Tkinter event loop
root.mainloop()