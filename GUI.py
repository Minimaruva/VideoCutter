import tkinter as tk
from tkinter import filedialog, simpledialog
import random
import os
import pandas as pd
import random


class SimpleApp:
    def __init__(self, root):
        
        
        # App Name Label (big text within the window)
        
        
        # Quote Input
        
        
        # Button for Random Quote
        random_quote_btn = tk.Button(root, text="Get Random Quote", command=self.get_random_quote)
        random_quote_btn.pack(pady=5)
        
        # Button to Choose Photo/Video File
        file_button = tk.Button(root, text="Choose Photo/Video", command=self.choose_file)
        file_button.pack(pady=10)
        
        # Label to show the selected file
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=5)
        
        # Button to choose output folder
        folder_button = tk.Button(root, text="Choose Output Folder", command=self.choose_folder)
        folder_button.pack(pady=10)
        
        # Label to show the selected folder
        self.folder_label = tk.Label(root, text="Output folder: ./output (default)")
        self.folder_label.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.pack(pady=20)

        # Store the file path and folder path, set default folder to "./output"
        self.file_path = None
        self.folder_path = "./output"  # Default output folder

    def get_random_quote(self):
        # Replace this with your random quote generation function
        random_quotes = [
            "The best way to get started is to quit talking and begin doing.",
            "The pessimist sees difficulty in every opportunity.",
            "Don’t let yesterday take up too much of today."
        ]
        random_quote = random.choice(random_quotes)
        self.quote_entry.delete(0, tk.END)  # Clear the entry field
        self.quote_entry.insert(0, random_quote)

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Select a Photo or Video",
            filetypes=[("All Files", "*.*"), ("Image/Video Files", "*.jpg;*.jpeg;*.png;*.mp4;*.mov")]
        )
        if self.file_path:
            self.file_label.config(text=f"File selected: {self.file_path}")
        else:
            self.file_label.config(text="No file selected")
    
    def choose_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select Output Folder")
        if self.folder_path:
            self.folder_label.config(text=f"Output folder: {self.folder_path}")
        else:
            self.folder_label.config(text="Output folder: ./output (default)")
            self.folder_path = "./output"  # Reset to default if none selected

    def submit(self):
        # Action when the submit button is clicked
        quote = self.quote_entry.get()
        
        # If no file is selected or output folder doesn't exist, show a warning (optional)
        if not self.file_path:
            print("Error: No file selected.")
            return

        # Ensure output folder exists (create it if it doesn't)
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        # Proceed with the submission logic
        print(f"Quote: {quote}")
        print(f"File Path: {self.file_path}")
        print(f"Output Folder: {self.folder_path}")
        
        # You can add your processing function here
        # e.g., process_video(self.file_path, quote, self.folder_path)
        
        # Close the app after submit
        self.root.destroy()


def random_quote():
    global quote_entry
    try:
        quotes_df = pd.read_csv("./assets/filtered_data.csv", sep=";")
        random_row = random.randint(1, len(quotes_df))
        quote = quotes_df.loc[random_row]["QUOTE"]
    except:
        quote = "Quotes not found"

    quote_entry.delete("1.0", tk.END)
    quote_entry.insert("1.0", quote)
    
def import_file():
    file_path = filedialog.askopenfilename(title="Select a file")


root = tk.Tk()
root.title("EasyReel by Vlad")
root.geometry("400x500")
root.configure(bg='#72BF78')

app_label = tk.Label(root, text="EasyReel\nMaking brainrot has never been easier!", font=("Arial", 14), bg='#72BF78')
app_label.pack()

# Quote frame
quote_frame = tk.Frame(root, bg="#A0D683")
quote_label = tk.Label(quote_frame, text="Enter your quote here", bg="#A0D683")
quote_entry = tk.Text(quote_frame, width=45, height=2, bg="#FEFF9F")

random_quote_button = tk.Button(quote_frame, text="Random quote", command=random_quote, bg="#FEFF9F", relief=tk.FLAT)

quote_label.pack(pady=5)
quote_entry.pack(padx=5)
random_quote_button.pack(pady=10)
quote_frame.pack()

# File uploader frame
file_frame = tk.Frame(root, bg="#A0D683")
file_label = tk.Label(file_frame, text="Choose your file (photo or image)", bg="#A0D683")
file_button = tk.Button(file_frame, text="Import file", command=import_file, bg="#FEFF9F", relief=tk.FLAT)

file_label.pack(padx=95)
file_button.pack(pady=10)
file_frame.pack(pady=10)

quote_text = quote_entry.get("1.0", tk.END)

# app = SimpleApp(root)
root.mainloop()
