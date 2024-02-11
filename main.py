import os, shutil

path = r"C:\Users\andre\Downloads\testfolder\\"
print("\n\n")
filename = os.listdir(path) #names of all files in the directory "path"
print(filename);
#create folders for organization if not already made
folder_names = ['Math Class', "Chemistry Class", "AP Physics C Class"]
for loop in range(0, 3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in filename: 
    if "Math" in file and not os.path.exists(path + "Math Class\\" + file) and not "Math Class" in file:
        shutil.move(path+file, path +"Math Class\\"+file) 
    elif "Chem" in file and not os.path.exists(path + "Chemistry Class\\" + file):
        shutil.move(path+file, path +"Chemistry Class\\"+file) 
    elif "APC" in file and not os.path.exists(path + "AP Physics C Class\\" + file):
        shutil.move(path+file, path +"AP Physics C Class\\"+file) 

print("\n\n")
