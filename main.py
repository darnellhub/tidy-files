from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
from tkinter import ttk

window = Tk()
window.title("Tidy Files")
window.geometry("500x600")
window.columnconfigure(1, weight=1)
window.rowconfigure(3, weight=1)

SUBDIR = {
    "DOCUMENTS": [".numbers",".ppt", ".pptx", ".otf", ".xls", ".odt", ".ott", ".doc", ".ods", ".csv", ".pdf", ".docx", ".txt",
                  ".xlsx"],
    "IMAGES": [".HEIC",".heic", ".raw", ".tiff", ".eps", ".svg", ".jpg", ".JPG", ".PNG", ".jpeg", ".png", ".gif"],
    "AUDIO": [".flac", ".wma", ".mp3", ".m4a", ".wav"],
    "VIDEO": [".MOV", ".MP4", ".mkv", ".wmv", ".mpeg", ".mp4", ".mov", ".avi"],
    "SOFTWARE": [".msi",".exe", ".dmg", ".pkg",".bin"],
    "ZIP FILES": [".zip", ".rar", ".bz2"],
    "TORRENTS": [".torrent"],
    "PHOTOSHOP": [".psd", ".psdt"]
}

selected_folder = None
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')


def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    print(selected_folder)


def sort():
    if selected_folder is None:
        messagebox.showerror("Error", "Please select folder first")
        return

    # Create a progress bar and add it to the window
    progress = ttk.Progressbar(window, length=200)
    progress.grid(row=6, column=1, columnspan=2)

    # Set the progress bar to 0%
    progress.config(value=0)
    progress.update()

    total_files = len(os.listdir(selected_folder))
    files_sorted = 0
    files_sorted_by_subdir = {subdir: 0 for subdir in SUBDIR}

    for subdir, extensions in SUBDIR.items():
        subdir_path = os.path.join(selected_folder, subdir)
        os.makedirs(subdir_path, exist_ok=True)
        for file in os.listdir(selected_folder):
            for extension in extensions:
                if file.endswith(extension):
                    shutil.move(os.path.join(selected_folder, file), subdir_path)
                    files_sorted += 1
                    files_sorted_by_subdir[subdir] += 1
                    progress.config(value=(files_sorted / total_files) * 100)
                    progress.update()
    progress.config(value=100)

    row = 6
    # for subdir, count in files_sorted_by_subdir.items():
    #     Label(window, text=f"{count} {subdir} files sorted").grid(row=row, column=1, columnspan=2)
    #     row += 1
    # other()
    Label(window, text="Done", fg="green").grid(row=5, column=1, columnspan=2)
    display_files()


def other():
    other_path = os.path.join(selected_folder, "OTHER")
    os.makedirs(other_path, exist_ok=True)

    for file in os.listdir(selected_folder):
        if not any(file.endswith(extension) for subdir, extensions in SUBDIR.items() for extension in extensions):
            try:
                shutil.move(os.path.join(selected_folder, file), other_path)
            except:
                print("Some sort of error")
    display_files()


def display_files():
    files_frame = Frame(window)
    files_frame.grid(row=4, column=1, columnspan=2, sticky="nsew")

    listbox = Listbox(files_frame)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(files_frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    count = {subdir: 0 for subdir in SUBDIR}
    for subdir in SUBDIR:
        subdir_path = os.path.join(selected_folder, subdir)
        files = os.listdir(subdir_path)
        if not files:
            continue
        count[subdir] = len(files)
        for file in files:
            listbox.insert(END, file)
    label_text = "\n".join([f"{count[subdir]} {subdir}" for subdir in count if count[subdir] > 0])
    label = Label(window, text=label_text, font=("Arial", 12, "bold"))
    label.grid(row=6, column=1, columnspan=2)


select_folder_image = PhotoImage(file=os.path.join(images_dir, 'folder.png'))
select_folder_button = Button(window, image=select_folder_image, width=100, height=100, command=select_folder)

sort_image = PhotoImage(file=os.path.join(images_dir, 'sort.png'))
sort_button = Button(window, image=sort_image, width=100, height=100, command=sort)

select_folder_button.grid(row=1, column=1, padx=5, pady=5)
sort_button.grid(row=2, column=1, padx=5, pady=5)

app_name = Label(window, text="Effortlessly sort and organize\n your files into Folders", font=("Arial", 12, "bold"))
app_name.grid(row=7, column=1, columnspan=4, sticky="nsew")

window.columnconfigure(1, weight=1)
window.rowconfigure(7, weight=1)

window.mainloop()
