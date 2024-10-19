import tkinter as tk
from tkinter import filedialog, simpledialog
import random
import os
import pandas as pd
import random

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
    global file_path 
    file_path = filedialog.askopenfilename(title="Select a file")

def output_folder():
    global output_path
    output_path = filedialog.askdirectory(title="Select the output path")

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

duration_label = tk.Label(file_frame, text="Enter duration of video in seconds (optional)", bg="#A0D683")
duration_entry = tk.Entry(file_frame, width=45, bg="#FEFF9F")

# Frame inside of File frame for radio buttons
radio_frame = tk.Frame(file_frame, bg="#A0D683")
selected_value = ""
rb1 = tk.Radiobutton(radio_frame, text="img-to-img", variable=selected_value, value="img-to-img")
rb2 = tk.Radiobutton(radio_frame, text="img-to-video", variable=selected_value, value="img-to-video")
rb3 = tk.Radiobutton(radio_frame, text="video-to-video", variable=selected_value, value="video-to-video")


file_label.pack(padx=94)
file_button.pack(pady=10)
duration_label.pack(padx=10)
duration_entry.pack(padx=10)

rb1.grid(row=0, column=0, padx=10)
rb2.grid(row=0, column=1, padx=10)
rb3.grid(row=0, column=2, padx=10)
radio_frame.pack(padx=5, pady=10)

file_frame.pack(pady=10)

# Submit Frame
submit_frame = tk.Frame(root, bg="#A0D683")
output_path_label = tk.Label(submit_frame, text="Choose outputfolder (optional)", bg="#A0D683")
output_path_button = tk.Button(submit_frame, text="Choose output folder", command=output_folder, bg="#FEFF9F", relief=tk.FLAT)

output_path_label = tk.Label(submit_frame, text="Choose outputfolder (optional)", bg="#A0D683")
output_path_button = tk.Button(submit_frame, text="Choose output folder", command=output_folder, bg="#FEFF9F", relief=tk.FLAT)

output_path_label.pack(padx=94)
output_path_button.pack(pady=10)

duration_label.pack(padx=10)
duration_entry.pack(padx=10)

submit_frame.pack(pady=10)

quote_text = quote_entry.get("1.0", tk.END)

# app = SimpleApp(root)
root.mainloop()
