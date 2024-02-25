import tkinter as tk
from tkinter import filedialog

def srt_to_text(srt_path, save_path):
    try:
        with open(srt_path, "r", encoding="utf-8") as f:
            srt = f.readlines()

        with open(save_path, "w", encoding="utf-8") as f:
            f.writelines(srt[2::4])
        
        result_label.config(text="SRT to Text conversion completed!", fg="green")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def text_to_srt(old_srt_path, text_path, save_path):

    try: 
        with open(old_srt_path, "r", encoding="utf-8") as f:
            old_srt = f.readlines()

        with open(text_path, "r", encoding="utf-8") as f:
            text = f.read().strip()
            text = text.splitlines()
            text = [line + "\n" for line in text]

        old_srt[2::4] = text

        with open(save_path, "w", encoding="utf-8") as f:
            f.writelines(old_srt)

        result_label.config(text="Text to SRT conversion completed!", fg="green")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")
        
def browse_file(entry_var, **kwargs):
    filename = filedialog.askopenfilename(**kwargs)
    entry_var.set(filename)

def browse_save_file(entry_var, **kwargs):
    filename = filedialog.asksaveasfilename(**kwargs)
    entry_var.set(filename)

def convert_srt_to_text():
    srt_path = srt_entry.get()
    save_path = text_save_entry.get()

    if not srt_path or not save_path:
        result_label.config(text="Please specify both SRT file and Text save path!", fg="red")
        return

    srt_to_text(srt_path, save_path)
    
    # Clear entry fields after execution
    srt_entry_var.set("")
    text_save_entry_var.set("")

def convert_text_to_srt():
    old_srt_path = old_srt_entry.get()
    text_path = translated_txt_entry.get()
    save_path = srt_save_entry.get()

    if not old_srt_path or not text_path or not save_path:
        result_label.config(text="Please specify Old SRT, Translated Text, and SRT save paths!", fg="red")
        return

    text_to_srt(old_srt_path, text_path, save_path)

    # Clear entry fields after execution
    old_srt_entry_var.set("")
    translated_txt_entry_var.set("")
    srt_save_entry_var.set("")


# Create the main window
root = tk.Tk()
root.title("SRT Text Converter")
root.resizable(False, False)

# SRT to Text Conversion
srt_label = tk.Label(root, text="Select SRT File:")
srt_entry_var = tk.StringVar()
srt_entry = tk.Entry(root, textvariable=srt_entry_var, width=50)
srt_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(srt_entry_var, title="Select SRT File", filetypes=[("SRT files", "*.srt")]))

text_save_label = tk.Label(root, text="Save Text to:")
text_save_entry_var = tk.StringVar()
text_save_entry = tk.Entry(root, textvariable=text_save_entry_var, width=50)
text_save_browse_button = tk.Button(root, text="Browse", command=lambda: browse_save_file(text_save_entry_var, title="Select Save File", defaultextension=".txt", filetypes=[("Text files", "*.txt")]))

convert_srt_button = tk.Button(root, text="Convert SRT to Text", command=convert_srt_to_text)

# Text to SRT Conversion
old_srt_label = tk.Label(root, text="Select Old SRT File:")
old_srt_entry_var = tk.StringVar()
old_srt_entry = tk.Entry(root, textvariable=old_srt_entry_var, width=50)
old_srt_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(old_srt_entry_var, title="Select SRT File", filetypes=[("SRT files", "*.srt")]))

translated_txt_label = tk.Label(root, text="Select New Text File:")
translated_txt_entry_var = tk.StringVar()
translated_txt_entry = tk.Entry(root, textvariable=translated_txt_entry_var, width=50)
translated_txt_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(translated_txt_entry_var, title="Select Text File", filetypes=[("Test files", "*.txt")]))

srt_save_label = tk.Label(root, text="Save SRT to:")
srt_save_entry_var = tk.StringVar()
srt_save_entry = tk.Entry(root, textvariable=srt_save_entry_var, width=50)
srt_save_browse_button = tk.Button(root, text="Browse", command=lambda: browse_save_file(srt_save_entry_var, title="Select Save File", defaultextension=".srt", filetypes=[("SRT files", "*.srt")]))

convert_text_button = tk.Button(root, text="Convert Text to SRT", command=convert_text_to_srt)

# Result Label
result_label = tk.Label(root, text="")

# Layout
srt_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
srt_entry.grid(row=0, column=1, padx=5, pady=5)
srt_browse_button.grid(row=0, column=2, padx=10, pady=5)

text_save_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
text_save_entry.grid(row=1, column=1, padx=5, pady=5)
text_save_browse_button.grid(row=1, column=2, padx=10, pady=5)

convert_srt_button.grid(row=2, column=0, columnspan=3, pady=10)

old_srt_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
old_srt_entry.grid(row=3, column=1, padx=5, pady=5)
old_srt_browse_button.grid(row=3, column=2, padx=10, pady=5)

translated_txt_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
translated_txt_entry.grid(row=4, column=1, padx=5, pady=5)
translated_txt_browse_button.grid(row=4, column=2, padx=10, pady=5)

srt_save_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
srt_save_entry.grid(row=5, column=1, padx=5, pady=5)
srt_save_browse_button.grid(row=5, column=2, padx=10, pady=5)

convert_text_button.grid(row=6, column=0, columnspan=3, pady=10)

result_label.grid(row=7, column=0, columnspan=3)

root.mainloop()
