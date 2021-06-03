from tkinter import filedialog
from tkinter import *
import os
import shutil
import easygui
from tkinter import messagebox as mb

def open_window():
    read = easygui.fileopenbox()
    return read

def openFiles():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation',"File not found!")

def saveFiles():
    filename = filedialog.asksaveasfilename(initialdir='/',title='Save File',filetypes=(('Text File','txt.*'),('Jpeg Files','jpg.*'),('All Files','*')))
    textContent = "\r\nHello everyone.\r\n"
    myfile = open(filename, "w+")
    myfile.write(textContent)
    print("File saved as "+filename)
    label_file_explorer.configure(text="File saved as : "+filename)

def copyFiles():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation','File Copied!')

def deleteFiles():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation',"File not found!")

def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")

    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  

    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

def list_files():
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+',')
        i+=1
    mb.showinfo('confirmation',sortlist)
    
# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("300x500")
  
#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_make = Button(window,

                        text = "Browse Files", width =50,
                        command = make_folder)

button_save = Button(window,text = "save Files", width = 50,command=saveFiles )
  
button_list = Button(window,
                     text = "List all files", width=50,
                     command = list_files)
button_exit = Button(window,
                     text = "Exit", width=50,
                     command = exit)
button_openwindow = Button(window,
                     text = "Open window", width=50,
                     command = open_window)
button_open = Button(window,
                     text = "Open File", width=50,
                     command = openFiles)
button_copy = Button(window,
                     text = "copy File", width=50,
                     command = copyFiles)
button_delete = Button(window,
                     text = "Delete File", width=50,
                     command = deleteFiles)

label_file_explorer.grid(column = 1, row = 1)

button_make.grid(column = 1, row = 2)
  
button_save.grid(column = 1, row = 3)

button_list.grid(column = 1,row = 4)

button_openwindow.grid(column = 1,row = 5 )

button_open.grid(column = 1,row = 6)

button_copy.grid(column = 1,row = 7)

button_delete.grid(column = 1,row = 8)
  
button_exit.grid(column = 1,row = 9)
  


window.mainloop()