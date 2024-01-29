import os
from tkinter import filedialog

# Directory selector with config persistence and assigns output_path, if you want a working directory changer just add after Final_Directory: os.chdir(Final_Directory)

def Directory_Selector(): # call the function in a button which command section is: 'command = lambda: Directory_Selector'
    Change_Directory = filedialog.askdirectory(initialdir = Final_Directory, mustexist = True) #open the media explorer to select a directory (return directory)
    Random_variable_name = open('filename.txt', 'w', encoding = 'utf-8') #open filename.txt (it is supposed that there already is a directory in the filename.txt)
    Random_variable_name.write(Change_Directory) #writes the directory you chose in Change_Directory
    Random_variable_name.close() #don't know if it is necessary
    Direct(Change_Directory) #global Final Directory = Change_directory but it is being used in initialdir before and returns errror, so call a function to assign the directory/path to the variable Final_Directory
    
def Direct(Change): #random name
    global Final_Directory                                 # Directory() and Direct() are to change the directory of the file, but if you run the program for the first time
    Final_Directory = Change                               # it won't have a directory assigned in filename.txt so it would return an error, try avoid this you use try: --》except:
                                                           # to run it anyway, then it creates and writes in filename.txt the Desktop path, reads it and returns to Final_Directory

def Load_Directory():   #loads the last directory assigned
    try:
        Directory_existance = open('filename.txt', 'r', encoding = 'utf-8').read() #Try to open the filename.txt, if it doesn't work because there is no filename.txt then go to except
        return Directory_existance #return to Final_Directory
    except:
        if(os.path.exists('filename.txt') == False): #If it doesn't exist then create one by writing inside the .txt the directory of the Desktop
            
            open('filename.txt', 'w', encoding = 'utf-8').write(os.path.expanduser('~/Desktop')) #Thanks to that person in Stack Overflow. You can change it to the directory in which the .py is in with os.getcwd(), 
                                                                                                #but it would only be good if you installed the program somewhere that is not program files
                                                                                                #to change it to the Downloads directory just write '~/Downloads' instead of '~/Desktop'
        
        Path_to_return = open('filename.txt', 'r', encoding = 'utf-8').read() #Now open the filename.txt (read) and return the Directory of the Desktop
        return Path_to_return #return to Final_Directory

Final_Directory = Load_Directory() #can be called as Actual_Directory
