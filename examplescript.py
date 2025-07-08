import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
wallpapers_dir = "/home/andetsu/.config/Wallpapers/" #Where your wallpapers are located.
oldwall_dir = "/home/andetsu/.config/hypr/wallpaper" #Name and directory of the wallpaper link file to create (do not change).
scripts_dir = "/home/andetsu/.config/hypr/scripts/" #Where your scripts (This script) are located.
#examplelist = ["item1", "item2", "item3"]
def init():
    root = ThemedTk(theme="black")
    try:
        wf = open(scripts_dir + "wallpaperfile.txt", "r")
        cwp = wf.read()
        print("Current Wallpaper:", cwp)
        wf.close()
    except FileNotFoundError:
        wf = open(scripts_dir + "wallpaperfile.txt", "w")
        wf.close()
        print("Couldn't read current wallpaper file. Created a new current wallpaper file, will record wallpaper changes to the file")
    

    
    title_label = ttk.Label(root, text="Ande's Wallpaper Changer",font=("Arial", 24))
    title_label.pack()
    wallpaper_frame = ttk.Frame(root)
    wallpaper_frame.pack()
    cwp_label = ttk.Label(wallpaper_frame, text=f"Current Wallpaper: ",font=("Arial", 18))
    cwp_label.pack(side=tk.LEFT)
    acwp_label = tk.Label(wallpaper_frame, text=f"{cwp}",fg = "red" ,bg = "#3c3f41",font=("Arial", 18))
    acwp_label.pack(side=tk.LEFT)
    ttk.Label(root, text="Choose a wallpaper from the list and hit 'Change Wallpaper' button.", font=("Arial", 18)).pack()
    examplelist1 = os.listdir('/home/andetsu/.config/Wallpapers/')
    examplelist = []
    for i in examplelist1:
            if '.png' in i or '.jpg' in i or '.jpeg' in i or '.webp' in i:
                examplelist.append(i)
    elistbox = tk.Listbox(root,bg ="#3c3f41",fg="#ffffff", font=("Arial", 12))
    elistbox.pack(pady=20,padx=10,fill=tk.BOTH,expand=True)
    elistbox.delete(0, tk.END)
    counter = 0
    draw(examplelist, elistbox, root)

def draw(validwalls, wplistbox, root):
    
    root.title("Experimenting")
    root.geometry("900x600")
    style=ttk.Style()
    style.configure("Centered.TButton",font = ("Segoe UI", 17), anchor="center")
    counter=0
    for i in validwalls:
        wplistbox.insert(tk.END, f"ID: {counter}, Name: {i}")
        counter += 1
    
    
    def on_select(validwalls):
        selected_index = wplistbox.curselection()
        if selected_index:
            value = wplistbox.get(selected_index[0])
            fixedvalue = value.replace(",", "")
            seperatedvalue = fixedvalue.split()
            print(seperatedvalue)
            for i in seperatedvalue:
                print(i)
                try:
                    i = int(i)
                    valuez = i
                    break
                except Exception as e:
                    pass
            print(f"{valuez}")
            messagebox.showinfo("", f"{valuez}")
            #wallpaper_name = "/home/andetsu/.config/Wallpapers/" + examplelist[valuez]
            try:
                foe = open(scripts_dir + "lastext.txt", "r") # Try to find last extension of wallpaper
            except FileNotFoundError:
                foe = open(scripts_dir + "lastext.txt", "w") # If last extension file is not found, create one and obtain the extension from hyprpaper config
                f = open("/home/andetsu/.config/hypr/hyprpaper.conf", "r")
                posext = [] # Possible extensions list
                for i in f: # Extension Finder (The for loop loops through the lines of hyprpaper.conf, and when it fins a valid extension; sets it as old extension)
                    posext.append(i)
                for i in posext:
                    if '.png' in i:
                        foe.write(".png")
                        break
                    if '.jpg' in i:
                        foe.write(".jpg")
                        break
                    if '.jpeg' in i:
                        foe.write(".jpeg")
                        break
                    if '.webp' in i:
                        foe.write(".webp")
                        break
                foe.close()
                foe = open(scripts_dir + "lastext.txt", "r")
        
            oldextension = foe.read()
            foe.close()
            try:
                wallpaper_name = "/home/andetsu/.config/Wallpapers/" + validwalls[valuez]# Set the wallpaper name so the script can now what to change the wallpaper to
            except IndexError:
                messagebox.showwarning("Warning", "Wallpaper ID invalid!")
                #actionf(validwalls)
            if " " in wallpaper_name:
                wallpaper_name1 = wallpaper_name.replace(" ","")
                print(wallpaper_name)
                print(wallpaper_name1)
                os.system(f'mv "{wallpaper_name}" "{wallpaper_name1}"')
                wallpaper_name = wallpaper_name1
            if "(" in wallpaper_name or ")" in wallpaper_name:
                wallpaper_name2 = wallpaper_name.replace("(", "")
                wallpaper_name2 = wallpaper_name2.replace(")", "")
                os.system(f'mv "{wallpaper_name}" "{wallpaper_name2}"')
                wallpaper_name = wallpaper_name2

            
            
            print(wallpaper_name)
            if '.png' in wallpaper_name:
                extension = ".png"
            elif '.jpg' in wallpaper_name:
                extension = ".jpg"
            elif '.jpeg' in wallpaper_name:
                extension = ".jpeg"
            elif '.webp' in wallpaper_name:
                extension = ".webp"
            wf = open(scripts_dir + "wallpaperfile.txt", "w")
            wf.write(wallpaper_name.replace(wallpapers_dir, "")) # Write the new wallpaper
            wf.close()
            foe = open(scripts_dir + "lastext.txt", "w")
            foe.write(extension)
            foe.close()
            os.system("rm -r " + oldwall_dir + oldextension) # Delete old wallpaper symlink
            os.system("ln -s "+ wallpaper_name + " " + oldwall_dir + extension) # Create new wallpaper symlink
            replace(extension, oldextension) # Actual wallpaper changer function
    def refresh(root):
        root.destroy()
        init()

    def rename(wplistbox, validwalls):
        selected_index = wplistbox.curselection()
        if selected_index:
            value = wplistbox.get(selected_index[0])
            fixedvalue = value.replace(",", "")
            seperatedvalue = fixedvalue.split()
            print(seperatedvalue)
            for i in seperatedvalue:
                print(i)
                try:
                    i = int(i)
                    valuez = i
                    break
                except Exception as e:
                    pass
        rename_window = tk.Toplevel()
        rename_window.title("Renaming")
        rename_window.geometry("600x400")
        rename_window.configure(bg="#3c3f41")
        try:
            label = ttk.Label(rename_window, text=f"You are renaming: {validwalls[valuez]}",font = ("Segoe UI", 17))
            label.pack()
        except UnboundLocalError:
            messagebox.showwarning("Error", "Are you sure you selected a wallpaper?")
            rename_window.destroy()

        rename_input = ttk.Entry(rename_window, width=25)
        rename_input.pack(pady=10)


        

        def actualrename(validwalls):
            filename = validwalls[valuez]
            if '.png' in filename:
                ext = ".png"
            elif '.jpg' in filename:
                ext = ".jpg"
            elif '.jpeg' in filename:
                ext = ".jpeg"
            elif '.webp' in filename:
                ext = ".webp"
            os.chdir(wallpapers_dir)
            os.system(f'mv "{filename}" "{rename_input.get()}"' + ext)
            messagebox.showinfo("Success", "Successfully renamed wallpaper.")
            refresh(root)
            kill()

        def kill():
            rename_window.destroy()
    
        buttons_frame = ttk.Frame(rename_window)
        buttons_frame.pack(pady=20)
        rename_button = ttk.Button(buttons_frame, text="Rename!", style="Centered.TButton", command=lambda: actualrename(validwalls))
        rename_button.pack(side=tk.LEFT, padx=5)
        cancel_button = ttk.Button(buttons_frame, text="Cancel", style="Centered.TButton", command=kill)
        cancel_button.pack(side=tk.LEFT, padx=5)

    def killroot():
        exit()
    def information():
        messagebox.showinfo("About","About WallpaperChanger\nThis is a simple wallpaper changing script made for hyprpaper\nChoose a wallpaper from the list (click on it) and hit Change Wallpaper to change to it.\nYou need to edit the script to enter your directories first.\nMade by yours truly, andetsu.")
    
    def preview(wplistbox, validwalls):
        selected_index = wplistbox.curselection()
        if selected_index:
            value = wplistbox.get(selected_index[0])
            fixedvalue = value.replace(",", "")
            seperatedvalue = fixedvalue.split()
            print(seperatedvalue)
            for i in seperatedvalue:
                print(i)
                try:
                    i = int(i)
                    valuez = i
                    break
                except Exception as e:
                    pass
        img=Image.open(wallpapers_dir + validwalls[valuez])
        width, height = img.size
        print(width, height)
        if width >= 3840 or height >= 2400:
            if width >= 3840:
                width = int(width/2)
            if height >= 2400:
                height = int(height/2)
            img = img.resize((int(width),int(height)))
        preview_window = tk.Toplevel()
        preview_window.title("Preview")
        preview_window.geometry(f"{width}x{height}")

        
        tk_img = ImageTk.PhotoImage(img)
        image_label = ttk.Label(preview_window, image=tk_img)
        image_label.pack()

        preview_window.bind("<Escape>", lambda e: preview_window.destroy())

    
    
    

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=20)
    examplebutton = ttk.Button(button_frame, text="Change Wallpaper", style="Centered.TButton", command=lambda: on_select(validwalls))
    examplebutton.pack(side=tk.LEFT, padx=5)
    refreshbutton = ttk.Button(button_frame, text="Refresh List", style="Centered.TButton", command=lambda: refresh(root))
    refreshbutton.pack(side=tk.LEFT,padx=5)
    renamebutton = ttk.Button(button_frame, text="Rename", style="Centered.TButton", command=lambda: rename(wplistbox, validwalls))
    renamebutton.pack(side=tk.LEFT,padx=5)
    renamebutton = ttk.Button(button_frame, text="More Info", style="Centered.TButton", command=information)
    renamebutton.pack(side=tk.LEFT,padx=5)
    previewbutton = ttk.Button(button_frame, text="Preview", style="Centered.TButton", command=lambda: preview(wplistbox, validwalls))
    previewbutton.pack(side=tk.LEFT,padx=5)
    quitbutton = ttk.Button(button_frame, text="Quit", style="Centered.TButton",  command=killroot)
    quitbutton.pack(side=tk.LEFT,padx=5)
    root.configure(bg="#3c3f41")
    root.mainloop() 

def replace(extension, oldextension):
    f = open("/home/andetsu/.config/hypr/hyprpaper.conf", "r") # Read hyprpaper config and get the old extension
    configeditor = []
    for line in f:
        configeditor.append(line)
    print(*configeditor)
    line1 = configeditor[0]
    line2 = configeditor[1]
    print(line1, line2)
    print(oldextension, extension)
    line1 = line1.replace(oldextension, extension)
    line2 = line2.replace(oldextension, extension)
    print(line1, line2)
    f.close()
    f = open("/home/andetsu/.config/hypr/hyprpaper.conf", "w") # Open hyprpaper config in read write mode to write new file path and extension
    f.write(line1)
    f.write(line2)
    f.close()
    #os.system("nohup /home/andetsu/rshyprpaper.sh")
    #os.system("pkill -f WallpaperChanger")
    os.system("nohup /home/andetsu/.config/hypr/scripts/rshypaper.sh & pkill -f WallpaperChanger") # Restart hyprpaper and close the app


init()


