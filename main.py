#Andrew Chen
#February 11 2024
#Sorts your downloads folder based on keywords in the file name

import os, shutil

path = r"C:\Users\andre\Downloads\\"

print("\n\n")
filename = os.listdir(path) #names of all files in the directory "path"
print(filename)

#create folders for organization if not already made
# folder_names = ['Math Class', "Chemistry Class", "AP Physics C Class"]
# for loop in range(0, 3):
#     if not os.path.exists(path + folder_names[loop]):
#         print(path + folder_names[loop])
#         os.makedirs(path + folder_names[loop])

for file in filename: 
    if "AP_IBHL_Chemistry" in file and not os.path.exists(path + "Chemistry\\" + file):
        shutil.move(path+file, path +"Chemistry\\"+file) 
    elif "_AP_Calculus" in file and not os.path.exists(path + "Calculus\\" + file):
        shutil.move(path+file, path +"Calculus\\"+file) 
    elif "PhysAPC" in file and not os.path.exists(path + "Physics C\\" + file):
        shutil.move(path+file, path +"Physics C\\"+file) 

print("\n\n")
