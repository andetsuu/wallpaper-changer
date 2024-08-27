import os
wallpapers_dir = "/home/andetsu/Desktop/Wallpapers/"
oldwall_dir = "/home/andetsu/.config/hypr/wallpaper"
def actionf():
    action = input("Choose an action (help for help): ")
    if action.lower() == "help":
        print("               ***Help menu***"                 )
        print("list/l - lists all currently available wallpapers (Just use changelist)")
        print("change/c - opens the changewallpaper dialog (OLD - NOT RECOMMENDED)")
        print("rename/r - rename a file")
        print("search/s - search for a file")
        print("preview/p - preview an image")
        print("changelist/cl - Change wallpaper using IDs from a list that has the wallpapers in wallpapers directory(NEW - RECOMMENDED)\n")
        print("***********************************************\n")
        actionf()
    elif action.lower() == "list" or action.lower() == "l":
        files = os.listdir(r'/home/andetsu/Desktop/Wallpapers/')
        for i in files:
            if '.png' in i or '.jpg' in i or '.jpeg' in i or '.webp' in i:
                print(i)
        actionf()
    elif action.lower() == "preview" or action.lower() == "p":
        preview()
    elif action.lower() == "rename" or action.lower() == "r":
        rename()
    elif action.lower() == "change" or action.lower() ==  "c":
        changewallpaper()
    elif action.lower() == "search" or action.lower() ==  "s":
        search()
    elif action.lower() == "changelist" or action.lower() == "cl":
        changewithlist()
def search():
    searching = input("Filename to search (You can include extension but you don't have to): ")
    os.chdir(wallpapers_dir)
    os.system("ls | grep " + searching)
    actionf()

def rename():
    filename = input("Filename to rename: ")
    ext = input("File extension: ")
    filename = filename + "." + ext
    if not os.path.exists(wallpapers_dir + filename):
        print("File does not exist!")
        actionf()
        
    replace = input("New name:")
    replace = replace + "." + ext
    os.chdir(wallpapers_dir)
    os.system("mv " + filename + " " + replace)
    print("Renamed")
    actionf()
 
def preview():
    filename = input("Filename to preview (Include extension) :")
    if not os.path.exists(wallpapers_dir + filename):
        print("File does not exist!")
        actionf()
    else:
        os.system("kitty --hold -T WallpaperPreview & brave " + wallpapers_dir + filename + " & pkill -f WallpaperPreview")
        actionf()


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
    os.system("nohup /home/andetsu/rshyprpaper.sh & pkill -f WallpaperChanger") # Restart hyprpaper and close the app

def changewallpaper():
    try:
        foe = open("lastext.txt", "r") # Try to find last extension of wallpaper
    except FileNotFoundError:
        foe = open("lastext.txt", "w") # If last extension file is not found, create one and obtain the extension from hyprpaper config
        f = open("/home/andetsu/.config/hypr/hyprpaper.conf", "r")
        posext = [] # Possible extensions list
        for i in f:
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
        
    foe = open("lastext.txt", "r")
    oldextension = foe.read()
    foe.close()
    try:
        wf = open("wallpaperfile.txt", "r")
        cwp = wf.read()
        print("Current Wallpaper:", cwp)
        wf.close()
    except FileNotFoundError:
        wf = open("wallpaperfile.txt", "w")
        wf.close()
        print("Couldn't read current wallpaper file. Created a new current wallpaper file, will record wallpaper changes to the file")

    wallpaper_name = input("Filename of the wallpaper (Do not include extension): ")
    possiblewallpaper = []
    validwallpaper = []
    files = os.listdir(r'/home/andetsu/Desktop/Wallpapers/')
    for i in files:
            if '.png' in i or '.jpg' in i or '.jpeg' in i or '.webp' in i:
                possiblewallpaper.append(i)

    for i in possiblewallpaper:
        if i == wallpaper_name + '.png' or i == wallpaper_name + '.jpg' or i == wallpaper_name + '.jpeg' or i == wallpaper_name + '.webp':
            validwallpaper.append(i)

    print(len(validwallpaper))

    if len(validwallpaper) == 1:
        selectionlist = os.listdir(r'/home/andetsu/Desktop/Wallpapers/')
        if wallpaper_name + '.png' in selectionlist:
            extension = ".png"
        elif wallpaper_name + '.jpg' in selectionlist:
            extension = ".jpg"
        elif wallpaper_name + '.jpeg' in selectionlist:
            extension = ".jpeg"
        if wallpaper_name + '.webp' in selectionlist:
            extension = ".webp"

    validextensions = []
    if len(validwallpaper) > 1:
        for i in validwallpaper:
            if '.png' in i:
                validextensions.append('.png')
            elif '.jpg' in i:
                validextensions.append('.jpg')
            elif '.jpeg' in i:
                validextensions.append('.jpeg')
            elif '.png' in i:
                validextensions.append('.webp')
        print("Valid Extensions:", *validextensions)

        extension = input("Extension of the wallpaper: ")
        if ".png" in extension or ".jpg" in extension or ".jpeg" in extension or ".webp" in extension:
            pass
        else:
            extension = "." + extension
    
    #oldextension = input("Extension of the old wallpaper: ")
    #extension = "." + extension
    #print(oldextension)
    
    

    try:
        wallpaper_name = wallpapers_dir + wallpaper_name + extension
    except UnboundLocalError:
        print("Cannot find the file you are referring to, please use the search action or check the wallpapers directory to see if the wallpaper exists.\n")
        actionf()
    #if not os.path.exists(wallpaper_name):
        #print("File does not exist!")
        #return
    #print(wallpaper_name)
    #print(oldwall_dir + oldextension)
    foe = open("lastext.txt", "w")
    foe.write(extension)
    foe.close()
    os.system("rm -r " + oldwall_dir + oldextension)
    os.system("ln -s "+ wallpaper_name + " " + oldwall_dir + extension)
    wf = open("wallpaperfile.txt", "w")
    wf.write(wallpaper_name.replace(wallpapers_dir, ""))
    wf.close()
    replace(extension, oldextension)

def changewithlist():
    foe = open("lastext.txt", "r")
    oldextension = foe.read()
    foe.close()

    files = os.listdir(wallpapers_dir)
    validwalls = []
    for i in files:
        if '.png' in i or '.jpg' in i or '.jpeg' in i or '.webp' in i:
            validwalls.append(i)
    if len(validwalls) == 0:
        print("You don't have any wallpapers available, please download some.")
        return
    else:
        pass

    print("***Available Wallpapers:***\n")
    counter = 0
    for i in validwalls:
        print("ID:", counter, "Name:" , i)
        counter += 1

    
    wf = open("wallpaperfile.txt", "r")
    cwp = wf.read()
    print("Current Wallpaper:", cwp)
    wf.close()
    choosewallpaper = int(input("Wallpaper ID (The one on the top is 0, next is 1 etc.): "))
    wallpaper_name = wallpapers_dir + validwalls[choosewallpaper]
    print(wallpaper_name)
    if '.png' in wallpaper_name:
        extension = ".png"
    elif '.jpg' in wallpaper_name:
        extension = ".jpg"
    elif '.jpeg' in wallpaper_name:
        extension = ".jpeg"
    elif '.webp' in wallpaper_name:
        extension = ".webp"
    wf = open("wallpaperfile.txt", "w")
    wf.write(wallpaper_name.replace(wallpapers_dir, ""))
    wf.close()
    foe = open("lastext.txt", "w")
    foe.write(extension)
    foe.close()
    os.system("rm -r " + oldwall_dir + oldextension)
    os.system("ln -s "+ wallpaper_name + " " + oldwall_dir + extension)
    replace(extension, oldextension)

print("Welcome to Ande's WallpaperChanger")
print("***WARNING: Changing anything other than the directory variables might break your hyprpaper config, please only change other stuff if you know what you are doing***")
print("***NOTE: This script uses hyprpaper to change wallpaper, if you use any other app to set wallpaper please edit the config to your liking.***\n")
actionf()
#changewithlist()