import os
wallpapers_dir = "/home/andetsu/.config/Wallpapers/" #Where your wallpapers are located.
oldwall_dir = "/home/andetsu/.config/hypr/wallpaper" #Name and directory of the wallpaper link file to create (do not change).
scripts_dir = "/home/andetsu/.config/hypr/scripts/" #Where your scripts (This script) are located.

def init():
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

    actionf(validwalls)

def actionf(validwalls):
    
    action = input("Choose an action (h for help, q to quit): ")
    if action.lower() == "help" or action.lower() == "h":
        print("               ***Help menu***\n"                 )
        print("list/l - lists all currently available wallpapers, Including their IDs")
        print("change/c - opens the changewallpaper dialog (OLD - NOT RECOMMENDED)")
        print("rename/r - rename a wallpaper")
        print("search/s - search for (a) wallpaper(s) and its/their ID(s)")
        print("preview/p - preview an image")
        print("changelist/cl - Change wallpaper using IDs from a list that has the wallpapers in wallpapers directory(NEW - RECOMMENDED)")
        print("currentwp/cw - Tells the last wallpapers name(you have to change wallpaper at least once for this to work.)")
        print("filter/f - Filter Wallpapers.")
        print("***********************************************\n")
        actionf(validwalls)
    elif action.lower() == "list" or action.lower() == "l":
        files = os.listdir(wallpapers_dir)
        #for i in files:
            #if '.png' in i or '.jpg' in i or '.jpeg' in i or '.webp' in i:
                #print(i)
        counter = 0
        for i in validwalls:
            print("ID:", counter, "Name:" , i)
            counter += 1
        actionf(validwalls)
    elif action.lower() == "preview" or action.lower() == "p":
        preview(validwalls)
    elif action.lower() == "rename" or action.lower() == "r":
        rename(validwalls)
    elif action.lower() == "change" or action.lower() ==  "c":
        changewallpaper()
    elif action.lower() == "search" or action.lower() ==  "s":
        search(validwalls)
    elif action.lower() == "changelist" or action.lower() == "cl":
        changewithlist(validwalls)
    elif action.lower() == "currentwp" or action.lower() == "cw":
        currentwp(validwalls)
    elif action.lower() == "filter" or action.lower() == "f":
        filterwallpapers(validwalls)
    elif action.lower() == "quit" or action.lower() == "q":
        exit()
    else: 
        print("Try typing help and pressing enter to see all available commands.")
        actionf(validwalls)
    

def search(validwalls):

    #print("***Available Wallpapers:***\n")
    counter = 0
    #for i in validwalls:
        #print("ID:", counter, "Name:" , i)
        #counter += 1

    searching = input("Filename to search: ")
    os.chdir(wallpapers_dir)
    for i in validwalls:
        if searching in i:
            print("ID:", counter, "Name:" , i)
        else:
            pass
        counter += 1
    #os.system("ls | grep " + searching)
    actionf(validwalls)

def rename(validwalls):

    print("***Available Wallpapers:***\n")
    counter = 0
    for i in validwalls:
        print("ID:", counter, "Name:" , i)
        counter += 1

    renamefile = int(input("Wallpaper ID to rename: "))
    replace = input("New Wallpaper Name:")
    
    filename = validwalls[renamefile]
    if '.png' in filename:
        ext = ".png"
    elif '.jpg' in filename:
        ext = ".jpg"
    elif '.jpeg' in filename:
        ext = ".jpeg"
    elif '.webp' in filename:
        ext = ".webp"
    replace = replace + ext
    os.chdir(wallpapers_dir)
    os.system("mv " + filename + " " + replace) # Renaming
    print("Renamed")
    actionf(validwalls)

    #OLD RENAME FUNCTION

    #filename = input("Filename to rename: ")
    #ext = input("File extension: ")
    #filename = filename + "." + ext
    #if not os.path.exists(wallpapers_dir + filename):
    #    print("File does not exist!")
    #    actionf(validwalls)
        
    #replace = input("New name:")
    #replace = replace + "." + ext
    #os.chdir(wallpapers_dir)
    #os.system("mv " + filename + " " + replace)
    #print("Renamed")
    #actionf(validwalls)
 
def preview(validwalls):

    print("***Available Wallpapers:***\n")
    counter = 0
    for i in validwalls:
        print("ID:", counter, "Name:" , i)
        counter += 1

    previewedfile = int(input("Insert Wallpaper ID to preview: "))
    filename = validwalls[previewedfile]
    os.system("kitty --hold -T WallpaperPreview & qimgv " + wallpapers_dir + filename + " & pkill -f WallpaperPreview") # Change brave to an image viewer app if you have one
    actionf(validwalls)

    #OLD PREVIEW FUNCTION

    #filename = input("Filename to preview (Include extension) :")
    #if not os.path.exists(wallpapers_dir + filename):
    #    print("File does not exist!")
    #    actionf(validwalls)
    #else:
    #    os.system("kitty --hold -T WallpaperPreview & brave " + wallpapers_dir + filename + " & pkill -f WallpaperPreview")
    #    actionf(validwalls)


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

def currentwp(validwalls):
    try:
        wf = open(scripts_dir + "wallpaperfile.txt", "r")
        cwp = wf.read()
        print("Current Wallpaper:", cwp)
        wf.close()
    except FileNotFoundError:
        wf = open(scripts_dir + "wallpaperfile.txt", "w")
        wf.close()
        print("Couldn't read current wallpaper file. Created a new current wallpaper file, will record wallpaper changes to the file")
    actionf(validwalls)

#NOTE: THIS IS THE OLD WALLPAPER CHANGING METHOD. I DO NOT RECOMMEND USING THIS
#NOTE 2: plz delete this.

def changewallpaper():
    try:
        foe = open(scripts_dir + "lastext.txt", "r") # Try to find last extension of wallpaper
        foe.close()
    except FileNotFoundError:
        foe = open(scripts_dir + "lastext.txt", "w") # If last extension file is not found, create one and obtain the extension from hyprpaper config
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
        
    foe = open(scripts_dir + "lastext.txt", "r")
    oldextension = foe.read()
    foe.close()
    try:
        wf = open(scripts_dir + "wallpaperfile.txt", "r")
        cwp = wf.read()
        print("Current Wallpaper:", cwp)
        wf.close()
    except FileNotFoundError:
        wf = open(scripts_dir + "wallpaperfile.txt", "w")
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
            elif '.webp' in i:
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
        actionf(validwalls)
    #if not os.path.exists(wallpaper_name):
        #print("File does not exist!")
        #return
    #print(wallpaper_name)
    #print(oldwall_dir + oldextension)
    foe = open(scripts_dir + "lastext.txt", "w")
    foe.write(extension) # Get Last Extension
    foe.close()
    os.system("rm -r " + oldwall_dir + oldextension) # Delete old wallpaper
    os.system("ln -s "+ wallpaper_name + " " + oldwall_dir + extension) # Create new wallpaper symlink
    wf = open(scripts_dir + "wallpaperfile.txt", "w")
    wf.write(wallpaper_name.replace(wallpapers_dir, "")) # Write latest wallpaper
    wf.close()
    replace(extension, oldextension)

# NEW CHANGE METHOD

def changewithlist(validwalls):
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

    print("***Available Wallpapers:***\n")
    counter = 0
    for i in validwalls:
        print("ID:", counter, "Name:" , i)
        counter += 1

    try:
        wf = open(scripts_dir + "wallpaperfile.txt", "r")
        cwp = wf.read()
        print("Current Wallpaper:", cwp)
        wf.close()
    except FileNotFoundError:
        wf = open(scripts_dir + "wallpaperfile.txt", "w")
        wf.close()
        print("Couldn't read current wallpaper file. Created a new current wallpaper file, will record wallpaper changes to the file")

    choosewallpaper = int(input("Wallpaper ID (The one on the top is 0, next is 1 etc.): "))
    try:
        wallpaper_name = wallpapers_dir + validwalls[choosewallpaper] # Set the wallpaper name so the script can now what to change the wallpaper to
    except IndexError:
        print("Wallpaper ID invalid!")
        actionf(validwalls)
    if " " in wallpaper_name:
        wallpaper_name1 = wallpaper_name.replace(" ","")
        print(wallpaper_name)
        print(wallpaper_name1)
        os.system(f'mv "{wallpaper_name}" "{wallpaper_name1}"')
        wallpaper_name = wallpaper_name.replace(" ","")
    if "(" in wallpaper_name or ")" in wallpaper_name:
        wallpaper_name2 = wallpaper_name.replace("(", "")
        wallpaper_name2 = wallpaper_name2.replace(")", "")
        os.system(f'mv "{wallpaper_name}" "{wallpaper_name2}"')
        wallpaper_name = wallpaper_name2

    #print(wallpaper_name)
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

#Wallpaper Filtering (Apply Filters to view specific wallpapers that match the criteria (WOW))

def filterwallpapers(validwalls):
    filtertype = input("Please choose a filter type: (f for all available filter types. q to cancel) ")
    if filtertype.lower() == "f":
        print("All Filter Types:\nExtension (e): Filter by file extension.\nLength (l): Filter by length\nContain (c): Contain a specific key combination\n---MORE SOON---")
        filterwallpapers(validwalls)
    elif filtertype.lower() == "e" or filtertype.lower() == "extension":
        extension = input("Please choose the extension to filter: ")
        counter = 0
        for i in validwalls:
            if f".{extension}" in i:
                print(f"ID: {counter} Name: {i}")
                counter+=1
            else:
                counter+=1
                pass
    elif filtertype.lower() == "l" or filtertype.lower() == "length":
        preferredlength = input("Length: ")
        equalornot = input("Equal to, Shorter than or Longer than?(e, s or l): ")
        if equalornot.lower() == "e":
            counter = 0
            for i in validwalls:
                if int(len(i) - 3) == int(preferredlength):
                    print(f"ID: {counter} Name: {i}")
                    counter += 1
                else:
                    counter += 1
                    pass
        elif equalornot.lower() == "s":
            counter = 0
            for i in validwalls:
                if int(len(i) - 3) < int(preferredlength):
                    print(f"ID: {counter} Name: {i}")
                    counter += 1
                else:
                    counter += 1
                    pass
        elif equalornot.lower() == "l":
            counter = 0
            for i in validwalls:
                if int(len(i) - 3) > int(preferredlength):
                    print(f"ID: {counter} Name: {i}")
                    counter += 1
                else:
                    counter += 1
                    pass
    #ADD HAS SPECIFIC KEY COMBINATIONS IN IT FILTER TOO!
    elif filtertype.lower() == "c" or filtertype.lower() == "contain":
        contain = input("What should the wallpaper name contain?: ")
        counter = 0
        for i in validwalls:
            if contain in i:
                print(f"ID: {counter} Name: {i}")
                counter+=1
            else:
                counter+=1
                pass
    elif filtertype.lower() == "q":
        pass

    actionf(validwalls)

print("Welcome to Ande's WallpaperChanger")
print("***WARNING: Changing anything other than the directory variables might break your hyprpaper config, please only change other stuff if you know what you are doing***")
print("***NOTE: This script uses hyprpaper to change wallpaper, if you use any other app to set wallpaper please edit the script to your liking.***\n")
print("Also there is no error handling for int(inputs)s (changing with ID) so please type actual numbers.\n")

#Functions used for testing new stuff

def testfunction(validwalls):
    for i in validwalls:
        print(i)
def testfunctiondependency():
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
    changewithlist(validwalls)

#actionf(validwalls)
init()
#changewithlist()
#testfunctiondependency()