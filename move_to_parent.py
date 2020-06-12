import os
import shutil

# list all the directories in current directory
dirs = [x[0] for x in os.walk("./")]

i = 0
for d in dirs:
    ## list all files in A/b/*, B/b/*, C/b/*...
    files_to_copy = os.listdir(os.path.join(d, ""))  
    print(files_to_copy)
    for f in files_to_copy:
        if f.endswith(".wav"):  ## copy the relevant files to dest
            shutil.copy(os.path.join(d, "", f), os.path.join("", f))
            os.rename(os.path.join("", f), str(i)+".wav")
            print("File number {}".format(i))
            i+=1
